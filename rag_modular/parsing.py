"""
parsing.py
Responsible for PDF/Markdown parsing related functionality
"""

import asyncio
import aiofiles
import tqdm
import random
import traceback
import datetime
from pathlib import Path
from typing import List

from llama_parse import LlamaParse

# PDF parsing instructions
# PDF parsing instructions
PARSE_INSTRUCTION = """
Convert the provided PDF document accurately to Markdown format, with special emphasis on table integrity, following these mandatory requirements:

1. Mandatory removal of all headers, footers, and footnotes:
   - Remove all header text (document titles, chapter names)
   - Remove all footer text (page numbers, dates, publication info)
   - Remove page numbers and repeated chapter references at page bottoms
   - Ignore all footnotes at page bottoms (numbered explanatory text like 1, 2, 3)

2. Table processing requirements (highest priority):
   - Tables must be 100% complete, no missing rows, columns, or cells allowed
   - Preserve and highlight table titles (e.g., "TABLE 2.1"), ensure they stay with table content
   - Resolve cross-page table issues: merge tables with same title or continuous tables
   - If a table spans multiple pages, identify and merge into a single continuous table, maintain alignment
   - Use standard Markdown table format, ensure column alignment
   - Tables may include "(CONTINUED)" markers, identify and merge these with original tables
   - If table content is split into multiple parts, merge into one table, not separate tables

3. Content processing:
   - Maintain original document structure and content integrity
   - Extract all figure descriptions and captions, maintain association with original figures
   - Preserve all numbers, units (e.g., CO₂, CH₄, N₂O), and special symbols, ensure correct conversion
   - Do not add content that doesn't exist in original
   - Do not omit any important content from original
   - Faithfully reflect original document section structure
   - **CRITICAL: Section 7.8 and all its subsections (7.8.1, 7.8.2, 7.8.3) MUST be extracted completely with ALL text content, including paragraphs, lists, and any embedded data points. Pay special attention to potential multi-column layouts within these sections (especially 7.8.1). Ensure text is extracted in the correct reading order (top-to-bottom, then left-to-right across columns). Do not merge text across columns incorrectly or omit text due to columns.**

No incomplete tables allowed under any circumstances. If tables span pages or content is scattered, merge all content into complete, continuous tables while preserving original table titles. Ensure the critical requirement for Section 7.8 extraction is fully met.
"""

async def parse_single_pdf(pdf_path: Path, md_dir: Path, llama_parse_api_key: str) -> Path:
    """
    Parse a single PDF file and convert to Markdown format

    Args:
        pdf_path (Path): PDF file path
        md_dir (Path): Markdown output directory
        llama_parse_api_key (str): LlamaParse API key
    Returns:
        Path: Generated Markdown file path
    """
    pdf_filename = pdf_path.stem
    document_path = md_dir / f"{pdf_filename}_parsed.md"

    # If already exists and not empty, return directly
    if document_path.exists() and document_path.stat().st_size > 100:
        return document_path

    # Create LlamaParse instance
    parser = LlamaParse(
        api_key=llama_parse_api_key,
        result_type="markdown",
        parsing_instruction=PARSE_INSTRUCTION,
        num_workers=2,
        max_timeout=5000,
        verbose=True,
        language="en",
    )

    max_retries = 3
    retry_count = 0
    last_exception = None

    while retry_count < max_retries:
        try:
            # Call LlamaParse to parse PDF (wrap synchronous method with thread pool)
            llama_parse_documents = await asyncio.to_thread(parser.load_data, str(pdf_path))
            # Check parsing results
            if not llama_parse_documents or all(not doc.text.strip() for doc in llama_parse_documents):
                raise ValueError(f"LlamaParse returned empty content: {pdf_path}")

            # Write to Markdown file
            async with aiofiles.open(document_path, "w", encoding='utf-8') as f:
                await f.write(f"# {pdf_filename}\n\n")
                for i, parsed_doc in enumerate(llama_parse_documents):
                    if parsed_doc.text and parsed_doc.text.strip():
                        await f.write(f"## Part {i+1}\n\n")
                        await f.write(parsed_doc.text)
                        await f.write("\n\n---\n\n")
            return document_path

        except Exception as e:
            last_exception = e
            retry_count += 1
            wait_time = (2 ** retry_count) * 2 + random.uniform(0, 1)
            await asyncio.sleep(wait_time)

    # Write failure report when failed
    async with aiofiles.open(document_path, "w", encoding='utf-8') as f:
        await f.write(f"# {pdf_filename} - Parsing Failed\n\n")
        await f.write(f"Error encountered while parsing this PDF. Last error message:\n{last_exception}\n\n")
        await f.write(f"Time: {datetime.datetime.now()}\n\n")
        await f.write(traceback.format_exc())
    return document_path

async def batch_parse_pdfs(pdf_dir: Path, md_dir: Path, llama_parse_api_key: str) -> List[Path]:
    """
    Batch parse all PDF files in a PDF folder

    Args:
        pdf_dir (Path): PDF folder path
        md_dir (Path): Markdown output directory
        llama_parse_api_key (str): LlamaParse API key
    Returns:
        List[Path]: List of all generated Markdown file paths
    """
    pdf_files = list(pdf_dir.glob("*.pdf"))
    if not pdf_files:
        return []

    md_dir.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(3)  # Control concurrency

    async def parse_with_semaphore(pdf_path):
        async with semaphore:
            return await parse_single_pdf(pdf_path, md_dir, llama_parse_api_key)

    tasks = [parse_with_semaphore(pdf_path) for pdf_path in pdf_files]
    md_files = []
    for task in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Parsing PDFs"):
        try:
            md_file = await task
            md_files.append(md_file)
        except Exception as e:
            print(f"Error occurred during parsing: {e}")
    return md_files
