"""
main.py
Command-line entry point, responsible for argument parsing and process dispatching.
"""

import argparse
import asyncio
from pathlib import Path
from config_table import LLAMA_API_KEY, LLM_API_KEY, PDF_DIR, MD_DIR, DB_PATH, LLM_MODEL, EMBED_MODEL,LLM_BASE_URL
from parsing_table import get_pdf_files, parse_pdfs_to_markdown
from vectordb_table import load_or_create_vectordb
from qa_chain_table import setup_qa_chain, query
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

async def main():
    """
    Main entry point, responsible for argument parsing and dispatching to various modules.
    """
    parser = argparse.ArgumentParser(description="Multi-document RAG system")
    parser.add_argument("--action", choices=["parse", "build_db", "query", "interactive", "all"], default="all", help="Action to perform")
    parser.add_argument("--question", type=str, default=None, help="The question to query")
    args = parser.parse_args()

    # 1. Parse PDFs
    if args.action in ["parse", "all"]:
        pdf_files = get_pdf_files(PDF_DIR)
        if pdf_files:
            parse_pdfs_to_markdown(pdf_files, MD_DIR, LLAMA_API_KEY)

    # 2. Build/Load Vector Database
    embeddings = FastEmbedEmbeddings(model_name=EMBED_MODEL)
    md_files = list(Path(MD_DIR).glob("*_parsed.md"))
    vectordb = await load_or_create_vectordb(DB_PATH, embeddings, md_files)

    # 3. Setup QA Chain
    llm = ChatOpenAI(
        model_name=LLM_MODEL,
        temperature=0,
        api_key=LLM_API_KEY,
        base_url = LLM_BASE_URL
    )
    qa_chain = setup_qa_chain(llm, vectordb)

    # 4. Interactive Q&A or Batch Q&A
    if args.action == "interactive":
        print("Entering interactive Q&A mode, type 'exit' to quit.")
        while True:
            q = input("Please enter your question: ").strip()
            if q.lower() in ["exit", "quit", "q"]:
                break
            result = await query(qa_chain, q)
            print(f"Answer: {result['result']}\n")
    elif args.action == "query" and args.question:
        result = await query(qa_chain, args.question)
        print(f"Question: {args.question}\nAnswer: {result['result']}\n")
    else:
        print("Process completed.")

if __name__ == "__main__":
    asyncio.run(main())
