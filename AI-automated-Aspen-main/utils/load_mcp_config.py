import os
from locations import CONFIG_DIR
import json

def load_mcp_config():
    with open(os.path.join(CONFIG_DIR, "mcp_config.json"), "r") as f:
        return json.load(f)

