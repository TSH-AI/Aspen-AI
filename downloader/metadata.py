"""
metadata.py
Responsible for metadata export, deduplication, loading, etc.
"""

import os
import pandas as pd
from typing import List, Dict, Optional
from .utils import get_logger

logger = get_logger(__name__)

def export_metadata(papers_info: List[Dict], save_path: str, config: Dict, filename: Optional[str] = None) -> Optional[str]:
    """
    Export paper metadata to CSV file
    Args:
        papers_info: List of paper metadata
        save_path: Save directory
        config: Configuration dictionary
        filename: Export filename
    Returns:
        Path of successfully exported file, returns None if failed.
    """
    if not papers_info:
        logger.warning("No paper metadata to export")
        return None
    filename = filename or config.get("metadata_file", "papers_metadata.csv")
    filepath = os.path.join(save_path, filename)
    try:
        export_columns = [
            "source", "title", "authors", "doi", "arxiv_id", "published_date", "year",
            "container_title", "venue", "publisher", "abstract", "keywords",
            "is_open_access", "url", "download_url", "local_path", "download_date",
            "citation_count", "type"
        ]
        df = pd.DataFrame(papers_info)
        for col in export_columns:
            if col not in df.columns:
                df[col] = None
        df = df[export_columns]
        for col in ["authors", "keywords"]:
            if col in df.columns:
                df[col] = df[col].apply(
                    lambda x: "; ".join(map(str, x)) if isinstance(x, list) else x
                )
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        logger.info(f"Paper metadata exported to: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"Failed to export paper metadata: {e}")
        return None

def remove_duplicates(papers: List[Dict]) -> List[Dict]:
    """
    Remove duplicate papers from search result list (based on DOI and title)
    Args:
        papers: List of papers with potential duplicates
    Returns:
        List of papers with duplicates removed.
    """
    unique_papers = []
    seen_keys = set()
    for paper in papers:
        doi = str(paper.get("doi", "")).lower()
        title = str(paper.get("title", "")).lower().strip()
        key = doi if doi else (title if title else None)
        if key is None:
            unique_papers.append(paper)
            continue
        if key not in seen_keys:
            unique_papers.append(paper)
            seen_keys.add(key)
        else:
            logger.debug(f"Duplicate paper found in current batch, removed: {title} (Key: {key})")
    return unique_papers
