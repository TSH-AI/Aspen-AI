"""
search.py
Responsible for all logic related to paper search (API encapsulation and result parsing for arxiv, crossref, unpaywall)
"""

import requests
import arxiv
import time
from typing import List, Dict, Any, Optional, Callable
from tqdm import tqdm
from .utils import get_logger

logger = get_logger(__name__)

# --- API Result Parsing Functions ---
def parse_arxiv_result(paper: arxiv.Result) -> Optional[Dict]:
    """Parse a single result from arXiv API"""
    try:
        return {
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "abstract": paper.summary,
            "url": paper.entry_id,
            "doi": None,
            "published_date": paper.published.strftime("%Y-%m-%d") if paper.published else None,
            "source": "arxiv",
            "arxiv_id": paper.get_short_id(),
            "keywords": [cat for cat in paper.categories],
            "download_url": paper.pdf_url,
            "is_open_access": True
        }
    except Exception as e:
        logger.error(f"Error parsing arXiv result: {getattr(paper, 'entry_id', None)}, error: {e}")
        return None

def parse_crossref_item(item: Dict) -> Optional[Dict]:
    """Parse a single result from Crossref API"""
    try:
        authors = []
        for author in item.get("author", []):
            name_parts = [author.get("given"), author.get("family")]
            authors.append(" ".join(filter(None, name_parts)))
        title = item.get("title", [""])[0] if item.get("title") else ""
        doi = item.get("DOI")
        published_parts = item.get("published", {}).get("date-parts", [[]])[0]
        published_date = None
        if published_parts:
            try:
                if len(published_parts) == 3:
                    published_date = f"{published_parts[0]:04d}-{published_parts[1]:02d}-{published_parts[2]:02d}"
                elif len(published_parts) == 2:
                    published_date = f"{published_parts[0]:04d}-{published_parts[1]:02d}"
                elif len(published_parts) == 1:
                    published_date = f"{published_parts[0]:04d}"
            except (ValueError, TypeError):
                published_date = str(published_parts[0])
        return {
            "title": title,
            "authors": authors,
            "abstract": "",
            "url": f"https://doi.org/{doi}" if doi else None,
            "doi": doi,
            "published_date": published_date,
            "source": "crossref",
            "type": item.get("type"),
            "container_title": item.get("container-title", [""])[0] if item.get("container-title") else None,
            "keywords": item.get("subject", []),
            "is_open_access": False
        }
    except Exception as e:
        logger.error(f"Error parsing Crossref result: {item.get('DOI')}, error: {e}")
        return None

# --- Generic Paginated API Fetch Function ---
def fetch_paginated_results(
    api_config: Dict,
    base_url: str,
    query: str,
    max_results: int,
    params_builder: Callable,
    results_extractor: Callable,
    item_parser: Callable,
    headers: Dict,
    source_name: str,
    pagination_type: str = 'offset',
    limit_param_name: str = 'limit',
    offset_param_name: str = 'offset',
    page_param_name: str = 'page',
    cursor_param_name: str = 'cursor',
    next_cursor_extractor: Optional[Callable] = None,
    initial_page: int = 0
) -> List[Dict]:
    """
    Generic paginated API result fetching function, applicable to Crossref, etc.
    """
    if not api_config.get("enabled", False):
        logger.info(f"Skipping disabled data source: {source_name}")
        return []
    limit_per_page = api_config.get("limit_per_page", 100)
    delay = api_config.get("delay", 0.5)
    api_key = api_config.get("api_key")
    if api_config.get("requires_key", False) and not api_key:
        logger.warning(f"{source_name} API requires API Key, but not provided in configuration. Skipping search.")
        return []
    logger.info(f"Searching from {source_name}: {query}, max results: {max_results}")
    final_results = []
    current_page_or_offset = initial_page
    next_cursor = None
    total_fetched = 0
    retries = 0
    max_retries = 3
    while total_fetched < max_results:
        page_limit = min(limit_per_page, max_results - total_fetched)
        params = params_builder(query, page_limit, current_page_or_offset, next_cursor)
        current_headers = headers.copy()
        if api_key and api_config.get("key_in_header", False):
            current_headers[api_config["key_header_name"]] = api_key
        elif api_key and api_config.get("key_in_params", False):
            params[api_config["key_param_name"]] = api_key
        try:
            logger.debug(f"{source_name} API request URL: {base_url}, Params: {params}")
            response = requests.get(base_url, params=params, headers=current_headers, timeout=30)
            if response.status_code == 429:
                logger.warning(f"Reached {source_name} API rate limit, waiting 60 seconds before retrying (attempt {retries + 1}/{max_retries})...")
                time.sleep(60)
                retries += 1
                if retries >= max_retries:
                    logger.error(f"Reached max retries for {source_name} API, stopping search")
                    break
                continue
            elif response.status_code == 401:
                logger.error(f"{source_name} API Key is invalid or expired, please check configuration. Stopping search.")
                break
            elif response.status_code >= 500:
                logger.error(f"{source_name} API server error ({response.status_code}), waiting 10 seconds before retrying (attempt {retries + 1}/{max_retries})...")
                time.sleep(10)
                retries += 1
                if retries >= max_retries:
                    logger.error(f"Reached max retries for {source_name} API (server error), stopping search")
                    break
                continue
            response.raise_for_status()
            data = response.json()
            retries = 0
            page_items = results_extractor(data)
            if not page_items:
                logger.info(f"{source_name} API returned no more results")
                break
            parsed_count = 0
            for item in page_items:
                parsed_item = item_parser(item)
                if parsed_item:
                    final_results.append(parsed_item)
                    total_fetched += 1
                    parsed_count += 1
                    if total_fetched >= max_results:
                        break
            if total_fetched >= max_results:
                break
            if pagination_type == 'offset':
                current_page_or_offset += len(page_items)
            elif pagination_type == 'page':
                current_page_or_offset += 1
            elif pagination_type == 'cursor' and next_cursor_extractor:
                next_cursor = next_cursor_extractor(data)
                if not next_cursor:
                    logger.info(f"{source_name} API did not return a next page cursor")
                    break
            else:
                logger.error(f"Unsupported pagination type or missing cursor extractor: {pagination_type}")
                break
            time.sleep(delay)
        except requests.exceptions.RequestException as e:
            logger.error(f"{source_name} search failed (Page/Offset: {current_page_or_offset}): {e}")
            retries += 1
            if retries >= max_retries:
                logger.error(f"Reached max retries for {source_name} API (network error), stopping search")
                break
            time.sleep(10)
            continue
        except Exception as e:
            logger.error(f"Error processing {source_name} response (Page/Offset: {current_page_or_offset}): {e}")
            break
    logger.info(f"Found {len(final_results)} related papers from {source_name}")
    return final_results

def get_open_access_info(papers, config):
    """
    Use Unpaywall API to get open access information for papers
    Args:
        papers: List of paper metadata
        config: Dictionary of configuration (needs apis.unpaywall configuration)
    Returns:
        List of paper metadata with updated OA information and download links
    """
    api_config = config["apis"]["unpaywall"]
    if not api_config.get("enabled", False):
        return papers
    logger.info(f"Getting open access information for {len(papers)} papers from Unpaywall")
    email = api_config.get("email")
    if api_config.get("requires_email", False) and not email:
        logger.warning("Unpaywall API requires email, but not found in configuration. Skipping open access check.")
        return papers
    base_url = api_config["base_url"]
    delay = api_config.get("delay", 0.2)
    updated_papers = []
    with tqdm(total=len(papers), desc="Unpaywall OA check") as pbar:
        for paper in papers:
            if not paper.get("doi"):
                updated_papers.append(paper)
                pbar.update(1)
                continue
            if paper.get("download_url") and paper["download_url"].startswith(('http', 'https')):
                paper["is_open_access"] = True
                updated_papers.append(paper)
                pbar.update(1)
                continue
            doi = paper["doi"]
            api_url = f"{base_url}{doi}?email={email}"
            try:
                response = requests.get(api_url, headers={"User-Agent": config.get("user_agent", "Mozilla/5.0")}, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    paper["is_open_access"] = data.get("is_oa", False)
                    paper["oa_locations"] = data.get("oa_locations", [])
                    pdf_urls = []
                    best_url = None
                    oa_location = data.get("best_oa_location")
                    if oa_location:
                        pdf_url = oa_location.get("url_for_pdf")
                        html_url = oa_location.get("url")
                        if pdf_url:
                            pdf_urls.append({"url": pdf_url, "source": "best_oa_location", "version": oa_location.get("version")})
                            best_url = pdf_url
                        elif html_url:
                            pdf_urls.append({"url": html_url, "source": "best_oa_location", "version": oa_location.get("version")})
                            best_url = html_url
                    for loc in data.get("oa_locations", []):
                        pdf_url = loc.get("url_for_pdf")
                        html_url = loc.get("url")
                        if pdf_url and not any(p["url"] == pdf_url for p in pdf_urls):
                            pdf_urls.append({"url": pdf_url, "source": "oa_location", "version": loc.get("version")})
                        elif html_url and not any(p["url"] == html_url for p in pdf_urls):
                            pdf_urls.append({"url": html_url, "source": "oa_location", "version": loc.get("version")})
                    paper["pdf_urls"] = pdf_urls
                    if best_url:
                        paper["download_url"] = best_url
                elif response.status_code == 404:
                    logger.debug(f"DOI {doi} not found in Unpaywall")
                    paper["is_open_access"] = False
                else:
                    logger.warning(f"Encountered an issue fetching OA information for DOI {doi}: {response.status_code}")
                time.sleep(delay)
            except requests.exceptions.Timeout:
                logger.error(f"Timeout fetching OA information for DOI {doi}")
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch OA information for DOI {doi}: {e}")
            except Exception as e:
                logger.error(f"Unknown error processing OA information for DOI {doi}: {e}")
            updated_papers.append(paper)
            pbar.update(1)
            pbar.set_postfix({"With Download Link": sum(1 for p in updated_papers if p.get("download_url"))})
    open_access_count = sum(1 for p in updated_papers if p.get("is_open_access"))
    with_download_url = sum(1 for p in updated_papers if p.get("download_url"))
    logger.info(f"OA check completed: {open_access_count} open access papers, {with_download_url} with download links")
    return updated_papers

# Specific search_arxiv, search_crossref, get_open_access_info functions are recommended to call this file's parsing and fetch functions in the main flow assembly
