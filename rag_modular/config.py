"""
config.py
Centralized management of global configuration parameters, such as API Keys, paths, model names, etc.
"""

import os

# LlamaParse API Key
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY",  "<your api key>")
# Large Language Model API Key
LLM_API_KEY = os.getenv("LLM_API_KEY", "<your api key>") 
# PDF file directory
PDF_DIR = os.getenv("PDF_DIR", "carbon_papers")
# Parsed Markdown file directory
MD_DIR = os.getenv("MD_DIR", "parsed_docs")
# Vector database path
DB_PATH = os.getenv("DB_PATH", "db_carbon_papers")
# Large Language Model name
LLM_MODEL = os.getenv("LLM_MODEL", "<your model>")


# Embedding model name
# EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-base-en-v1.5")  # Original model, may not be downloadable
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")  # Smaller and easier to download model

# Qwen API (Tongyi Qianwen)
QWEN_API_KEY = os.getenv("QWEN_API_KEY", "<your api key>")
QWEN_BASE_URL = os.getenv("QWEN_BASE_URL", "<your base url>")

# Backup API configuration (DeepSeek)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "<your api key>")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "<your base url>")

# LLM Base URL (for compatibility)
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "<your base url>")

# Local model configuration (if API is unavailable)
USE_LOCAL_MODEL = os.getenv("USE_LOCAL_MODEL", "false").lower() == "true"