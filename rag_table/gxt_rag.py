"""
gxt_rag.py
Simplified RAG query system for GXT cooling tower specifications.
"""

import os
import asyncio
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Set environment variable to disable tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from config_table import LLM_API_KEY_TABLE, DB_PATH_TABLE, MD_DIR_TABLE, LLM_MODEL_TABLE, EMBED_MODEL_TABLE, LLM_BASE_URL_TABLE
from qa_chain_table import setup_qa_chain, query
from vectordb_table import load_or_create_vectordb

from download_images import download_spec_images
from process_table import main as process_table_main


def check_existing_data():
    db_path_obj = Path(DB_PATH_TABLE)
    md_dir_obj = Path(MD_DIR_TABLE)
    
    # Check if the vector database directory and collection exist
    db_exists = db_path_obj.exists() and db_path_obj.is_dir() and (db_path_obj / 'collection' / 'all_documents_embeddings').exists()
    
    # Check if any parsed Markdown files exist
    md_exists = md_dir_obj.exists() and md_dir_obj.is_dir() and any(md_dir_obj.glob('*.md'))
    
    # Check specifically for the target parsed file
    target_md_file = md_dir_obj / 'gxt_specification_table_parsed.md'
    target_md_exists = target_md_file.exists()
    
    return db_exists, target_md_exists

async def get_gxt_table():
    db_exists, md_exists = check_existing_data()

    # If the Markdown file does not exist, start the automatic data preparation process
    if not md_exists:
        print("Parsed specification table Markdown file not found, generating automatically...")
        
        # Step 1: Download specification table images from the website
        TARGET_URL = "<your base url>"
        IMAGE_SAVE_DIR = "web_content"
        try:
            download_spec_images(TARGET_URL, IMAGE_SAVE_DIR, verbose=False)
        except Exception as e:
            print(f"Image download failed: {e}")
            return None

        # Step 2: Process images, extract table, and save as Markdown
        try:
            process_table_main(verbose=False)
        except Exception as e:
            print(f"Table processing failed: {e}")
            return None

        print("Automated data preparation complete.")

    # Initialize LLM and embeddings
    print("Initializing models and QA chain...")
    
    # Configure LLM with proper base URL from config
    llm = ChatOpenAI(
        model_name=LLM_MODEL_TABLE, 
        temperature=0, 
        api_key=LLM_API_KEY_TABLE,
        base_url=LLM_BASE_URL_TABLE,
        request_timeout=60, # Set a 60-second timeout to prevent premature errors
    )
    embeddings = FastEmbedEmbeddings(model_name=EMBED_MODEL_TABLE)

    # Load or create the vector database
    md_files = list(Path(MD_DIR_TABLE).glob("*.md"))
    if not md_files:
        print("Error: No Markdown files found after data preparation.")
        return None
        
    vectordb = await load_or_create_vectordb(DB_PATH_TABLE, embeddings, md_files)
    if not vectordb:
        print("Error: Failed to load or create the vector database.")
        return None

    # Set up the QA chain
    qa_chain = setup_qa_chain(llm, vectordb)

    # Perform the query
    question = "Give the table of SPECIFICATION FOR GXT SERIES"
    print(f"\n--- Querying ---\n{question}\n")
    result = query(qa_chain, question)
    
    # Return the result instead of printing it
    if result and "result" in result:
        return result["result"]
    else:
        print("Error: Query failed to produce a result.")
        return None

if __name__ == "__main__":
    # This block is for direct execution of the script
    print("Executing gxt_rag.py directly...")
    table_result = asyncio.run(get_gxt_table())
    if table_result:
        # Output the result
        print("\n--- Result ---")
        print(table_result) 
        print(table_result) 