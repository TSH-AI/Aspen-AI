"""
config.py
Centralized management of global configuration parameters, such as API Key, paths, model names, etc.
"""

import os

# LlamaParse API Key
LLAMA_API_KEY_TABLE = os.getenv("LLAMA_API_KEY_TABLE",  "<your api key>")

LLM_MODEL_TABLE = os.getenv("LLM_MODEL_TABLE", "<your model>")
LLM_API_KEY_TABLE = os.getenv("LLM_API_KEY_TABLE", "<your api key>")
LLM_BASE_URL_TABLE = os.getenv("LLM_BASE_URL_TABLE", "<your base url>")

# PDF file directory
PDF_DIR_TABLE = os.getenv("PDF_DIR_TABLE", "Web_PDF")

# Parsed Markdown file directory
MD_DIR_TABLE = os.getenv("MD_DIR_TABLE", "parsed_Web_PDF")

# Vector database path
DB_PATH_TABLE = os.getenv("DB_PATH_TABLE", "./db_Web_PDF")

# Large Language Model name
LLM_MODEL_TABLE = os.getenv("LLM_MODEL_TABLE", "<your model>")

# Embedding model name - use a more lightweight model to avoid network issues
EMBED_MODEL_TABLE = os.getenv("EMBED_MODEL_TABLE", "BAAI/bge-base-en-v1.5")