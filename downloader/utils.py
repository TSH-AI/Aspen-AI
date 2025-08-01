"""
utils.py
Stores common utility functions, such as logging configuration, configuration merging, helper functions, etc.
"""

import logging
from typing import Dict

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("paper_downloader.log"),
        logging.StreamHandler()
    ]
)

def get_logger(name=None):
    """
    Get logger instance for unified calling across modules.
    """
    return logging.getLogger(name)


def merge_configs(default: Dict, user: Dict) -> Dict:
    """
    Deep merge configuration dictionaries
    Args:
        default: Default configuration
        user: User custom configuration
    Returns:
        Merged configuration dictionary
    """
    merged = default.copy()
    for key, value in user.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value
    return merged

# Example structure
# def merge_configs(...):
#     pass

# def setup_logger(...):
#     pass
