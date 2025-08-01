"""
standards.py
Responsible for metadata acquisition and free download logic related to carbon emission standards
"""

# Standard-related code will be migrated here later

# Example structure
# def get_carbon_standards(...):
#     pass

# def download_free_standards(...):
#     pass

import os
import time
from typing import List, Dict, Optional
import requests
import pandas as pd
from .utils import get_logger

logger = get_logger(__name__)

def get_carbon_standards() -> List[Dict]:
    """
    Get international standard metadata related to carbon emission accounting
    Returns:
        List of dictionaries containing standard information
    """
    logger.info("Getting international standard metadata related to carbon emission accounting")
    standards = [
        # ... (omitted here, please copy the complete original standard list when migrating) ...
    ]
    return standards

def download_free_standards(standards: List[Dict], output_dir: str, config: Dict) -> List[Dict]:
    """
    Download carbon emission accounting standards with free access links
    Args:
        standards: List of standard metadata
        output_dir: Output directory
        config: Configuration dictionary
    Returns:
        List of download results
    """
    os.makedirs(output_dir, exist_ok=True)
    logger.info(f"Downloading free carbon emission standards to {output_dir}")
    results = []
    downloadable_standards = [s for s in standards if s.get("free_access")]
    if not downloadable_standards:
        logger.warning("No standards found with free download links")
        return results
    logger.info(f"Found {len(downloadable_standards)} standards that can be downloaded for free")
    for standard in downloadable_standards:
        standard_id = standard.get("standard_id")
        download_url = standard.get("free_access")
        title = standard.get("title")
        if not download_url:
            continue
        filename = f"standard_{standard_id.replace(':', '_').replace('/', '_')}.pdf"
        file_path = os.path.join(output_dir, filename)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 1024:
            logger.info(f"Standard '{title}' ({standard_id}) already exists, skipping download")
            standard["local_path"] = file_path
            results.append(standard)
            continue
        logger.info(f"Downloading standard: {title} ({standard_id})")
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(download_url, headers={"User-Agent": config.get("user_agent", "Mozilla/5.0")}, stream=True, timeout=120)
                response.raise_for_status()
                content_type = response.headers.get('Content-Type', '').lower()
                is_pdf = 'pdf' in content_type or 'application/octet-stream' in content_type
                if not is_pdf:
                    logger.warning(f"Warning: Downloaded content for standard '{title}' may not be PDF (Content-Type: {content_type})")
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                if os.path.getsize(file_path) < 1024:
                    logger.error(f"Download failed: Standard '{title}' file is too small, may be incomplete")
                    os.remove(file_path)
                    continue
                logger.info(f"Successfully downloaded standard: {title} ({standard_id})")
                standard["local_path"] = file_path
                results.append(standard)
                break
            except Exception as e:
                logger.error(f"Download failed (attempt {attempt + 1}/{max_retries}): {title}, error: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                else:
                    logger.error(f"Download of '{title}' reached maximum retry count, abandoning download")
        time.sleep(config.get("download_delay", 3))
    logger.info(f"Successfully downloaded {len(results)}/{len(downloadable_standards)} free standards")
    return results

def export_standards_metadata(standards: List[Dict], output_dir: str, filename: Optional[str] = None) -> Optional[str]:
    """
    Export standard metadata to CSV file
    Args:
        standards: List of standard metadata
        output_dir: Output directory
        filename: Output filename
    Returns:
        Saved file path
    """
    if not standards:
        logger.warning("No standard metadata to export")
        return None
    if filename is None:
        filename = "carbon_standards_metadata.csv"
    filepath = os.path.join(output_dir, filename)
    try:
        df = pd.DataFrame(standards)
        df.to_csv(filepath, index=False, encoding='utf-8')
        logger.info(f"Standard metadata exported to: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"Failed to export standard metadata: {e}")
        return None
