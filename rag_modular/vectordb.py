"""
vectordb.py
Responsible for vector database construction, loading, and management
"""

import asyncio
import tqdm
from pathlib import Path
from typing import List, Optional, Any

from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient

async def build_vectordb(md_files: List[Path], embeddings: Any, db_path: Optional[str] = None) -> Any:
    """
    Build vector database from Markdown files

    Args:
        md_files (List[Path]): List of Markdown file paths
        embeddings (Any): Embedding model instance
        db_path (Optional[str]): Vector database path
    Returns:
        Any: Qdrant database instance
    """
    all_docs_with_metadata = []
    for md_file in tqdm.tqdm(md_files, desc="Loading Markdown files"):
        try:
            loader = UnstructuredMarkdownLoader(str(md_file))
            loaded_documents = await asyncio.to_thread(loader.load)
            file_name = md_file.name
            for doc in loaded_documents:
                if 'metadata' not in doc or not isinstance(doc.metadata, dict):
                    doc.metadata = {}
                doc.metadata['filename'] = file_name
            all_docs_with_metadata.extend(loaded_documents)
        except Exception as e:
            print(f"Error loading file {md_file}: {e}")

    if not all_docs_with_metadata:
        print("Error: Failed to load any document fragments from Markdown files.")
        return None

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4096, chunk_overlap=512)
    chunks = text_splitter.split_documents(all_docs_with_metadata)
    print(f"Split documents into {len(chunks)} text chunks")

    # Create Qdrant vector database
    try:
        vectordb = await asyncio.to_thread(
            Qdrant.from_documents,
            chunks,
            embeddings,
            path=db_path,
            collection_name="all_documents_embeddings"
        )
        print(f"Successfully saved vector data to: {db_path}")
        return vectordb
    except Exception as e:
        print(f"Error creating Qdrant vector database: {e}")
        return None

async def load_or_create_vectordb(db_path: str, embeddings: Any, md_files: List[Path]) -> Any:
    """
    Load or create vector database

    Args:
        db_path (str): Vector database path
        embeddings (Any): Embedding model instance
        md_files (List[Path]): List of Markdown file paths
    Returns:
        Any: Qdrant database instance
    """
    db_path_obj = Path(db_path)
    collection_name = "all_documents_embeddings"

    # Check if Qdrant database exists
    qdrant_files_exist = db_path_obj.exists() and db_path_obj.is_dir() and \
                         any(f.name == 'collection' and f.is_dir() for f in db_path_obj.iterdir()) and \
                         (db_path_obj / 'collection' / collection_name).exists()
    if qdrant_files_exist:
        try:
            print(f"Attempting to load existing vector database from {db_path_obj}...")
            client = await asyncio.to_thread(QdrantClient, path=str(db_path_obj))
            await asyncio.to_thread(client.get_collection, collection_name=collection_name)
            vectordb = Qdrant(
                client=client,
                collection_name=collection_name,
                embeddings=embeddings,
            )
            print(f"Successfully loaded existing vector database '{collection_name}'.")
            return vectordb
        except Exception as e:
            print(f"Error loading existing vector database: {e}")
            print("Will attempt to rebuild vector database")

    # If loading fails or database/collection doesn't exist, rebuild
    print("Starting to build new vector database...")
    vectordb = await build_vectordb(md_files, embeddings, db_path)
    return vectordb
