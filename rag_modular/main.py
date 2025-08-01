"""
main.py
Command line entry point, responsible for parameter parsing and process scheduling
"""

import argparse
import asyncio
from pathlib import Path
from config import LLAMA_API_KEY, LLM_API_KEY, PDF_DIR, MD_DIR, DB_PATH, LLM_MODEL, EMBED_MODEL
from parsing import batch_parse_pdfs
from vectordb import build_vectordb, load_or_create_vectordb
from qa_chain import setup_qa_chain, query
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

async def main():
    """
    Main process entry point, responsible for parameter parsing and module scheduling
    """
    parser = argparse.ArgumentParser(description="Multi-document RAG system")
    parser.add_argument("--action", choices=["parse", "build_db", "query", "interactive", "all"], default="all", help="Action to execute")
    parser.add_argument("--question", type=str, default=None, help="Question to query")
    args = parser.parse_args()

    # 1. Parse PDFs
    if args.action in ["parse", "all"]:
        await batch_parse_pdfs(Path(PDF_DIR), Path(MD_DIR), LLAMA_API_KEY)

    # 2. Build/load vector database
    embeddings = FastEmbedEmbeddings(model_name=EMBED_MODEL)
    md_files = list(Path(MD_DIR).glob("*_parsed.md"))
    vectordb = await load_or_create_vectordb(DB_PATH, embeddings, md_files)

    # 3. Setup QA chain
    llm = ChatOpenAI(
        model_name=LLM_MODEL,
        temperature=0,
        openai_api_key=LLM_API_KEY,
        base_url = "<your base url>" 
    )
    qa_chain = setup_qa_chain(llm, vectordb)

    # 4. Interactive QA or batch QA
    if args.action == "interactive":
        print("Entering interactive QA mode, type 'exit' to quit.")
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
