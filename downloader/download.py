"""
download.py
Responsible for paper download related logic, including single download, batch download, download retry, filename generation, etc.
"""

import os
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Optional
import requests
from tqdm import tqdm
from .utils import get_logger

logger = get_logger(__name__)

DEFAULT_DOWNLOAD_DELAY = 3
DEFAULT_DOWNLOAD_WORKERS = 3


def download_paper(paper_info: Dict, save_path: str, config: Dict) -> bool:
    """
    Download a single paper with retry and file size checking
    Args:
        paper_info: Paper information dictionary
        save_path: Save directory
        config: Configuration dictionary
    Returns:
        Whether download was successful
    """
    download_url = paper_info.get("download_url")
    title = paper_info.get('title', 'Unknown Title')
    if not download_url:
        logger.debug(f"Paper '{title}' has no download link")
        return False
    # Filename generation logic is recommended to be extracted to utils later
    file_name = paper_info.get('file_name') or f"{title}.pdf"
    file_path = os.path.join(save_path, file_name)
    if os.path.exists(file_path) and os.path.getsize(file_path) > 1024:
        logger.debug(f"Paper '{title}' already exists and is valid, skipping download")
        paper_info["local_path"] = file_path
        return True
    elif os.path.exists(file_path):
        logger.warning(f"Paper '{title}' already exists but file is too small or invalid, attempting to re-download")
    logger.info(f"Downloading: {title} -> {file_path}")
    max_retries = 3
    download_delay = config.get("download_delay", DEFAULT_DOWNLOAD_DELAY)
    for attempt in range(max_retries):
        try:
            req_headers = {
                'User-Agent': config.get("user_agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"),
                'Accept': 'application/pdf, application/octet-stream, */*'
            }
            response = requests.get(download_url, headers=req_headers, stream=True, timeout=60, allow_redirects=True)
            response.raise_for_status()
            content_type = response.headers.get('Content-Type', '').lower()
            is_pdf = 'pdf' in content_type
            is_octet_stream = 'octet-stream' in content_type
            if not is_pdf and not is_octet_stream:
                logger.warning(f"Warning: Downloaded content for '{title}' may not be PDF (Content-Type: {content_type}) [{download_url}]")
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            if os.path.getsize(file_path) < 1024:
                logger.error(f"Download failed: '{title}' file is too small [{download_url}]")
                if os.path.exists(file_path):
                    try: os.remove(file_path)
                    except OSError: pass
                if attempt < max_retries - 1:
                    logger.info(f"Attempting to re-download '{title}' (attempt {attempt + 2}/{max_retries})...")
                    time.sleep(5)
                    continue
                else:
                    return False
            paper_info["local_path"] = file_path
            paper_info["download_date"] = datetime.now().strftime("%Y-%m-%d")
            logger.info(f"Successfully downloaded: {title}")
            time.sleep(download_delay)
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Download failed (attempt {attempt + 1}/{max_retries}): {title}, URL: {download_url}, error: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                logger.error(f"Download of '{title}' reached maximum retry count, abandoning download")
                return False
        except Exception as e:
            logger.error(f"Unknown error during download: {title}, error: {e}")
            return False
    return False

def batch_download(papers: List[Dict], save_path: str, config: Dict) -> int:
    """
    Batch download papers
    Args:
        papers: List of paper information
        save_path: Save directory
        config: Configuration dictionary
    Returns:
        Number of successfully downloaded papers
    """
    if not papers:
        logger.warning("No papers to download")
        return 0
    
    os.makedirs(save_path, exist_ok=True)
    download_workers = config.get("download_workers", DEFAULT_DOWNLOAD_WORKERS)
    
    logger.info(f"Starting batch download of {len(papers)} papers to {save_path}")
    successful_downloads = 0
    
    with ThreadPoolExecutor(max_workers=download_workers) as executor:
        futures = []
        for paper in papers:
            future = executor.submit(download_paper, paper, save_path, config)
            futures.append(future)
        
        with tqdm(total=len(papers), desc="Downloading papers") as pbar:
            for future in futures:
                try:
                    if future.result():
                        successful_downloads += 1
                except Exception as e:
                    logger.error(f"Error in download thread: {e}")
                pbar.update(1)
    
    logger.info(f"Batch download completed: {successful_downloads}/{len(papers)} papers downloaded successfully")
    return successful_downloads
