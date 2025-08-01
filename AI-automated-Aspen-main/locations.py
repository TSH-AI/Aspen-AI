import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

# create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

CONFIG_DIR = os.path.join(ROOT_DIR, "configs")




