# AI-automated-Aspen
This project aims to integrate Aspen series software with LLMs and MCP tools 

## Requirements

- Local docker-based MCP tools (refer to https://github.com/modelcontextprotocol/servers/tree/main).

See docs in Github and Filesystem servers to set up docker-based MCPs

- GitHub API key: see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

- Python 3.11+ (this is for later integration with Langgraph Studio)

## Quick start 

1. Python environment setup: `pip install -r requirements.txt`

2. Configuration: `configs/mcp_config.json` contains the configuration for the MCP tools. 

1. Add your GitHub API key to the `env` section. 

```json
    "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "<your_github_api_key>"
     },
```

2. Add the path to the `data` directory in the `filesystem` section. Please note that the path should be the absolute path to the local data directory. e.g., "C:\\Users\\...\\data". This folder will be the folder that the agents read from and write to. 

```json
    "filesystem": {
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "--mount", "type=bind,src=<your_absolute_path_to_local_data_directory> ,dst=/projects/data",
            "mcp/filesystem",
            "/projects"
        ],
        "transport": "stdio"
    }
```


## Usage: Training data collection 

The very first step of this project is to collect as many `.BKP` (Aspen Backup files) as possible and as diversed as possible. 

The current strategy is to use MCP tools, including GitHub and Serp tool, to locate `.BKP`files on the internet and provide according documentations on the `.BKP` files. 

It takes the following steps: 

1. run `python -m src.data_collection_github_agent.graph` to create lists of `.BKP` files from GitHub. The agent will automatically create a list of `.BKP` files and save it to the `data` directory. 

2. run `python -m scripts.create_download_list` to create a list of download links for the `.BKP` files. 

3. use third party tool to download the `.BKP` files from the download links. Recommend using `aria2` to download the files if you are on linux systems and `Xunlei` on windows systems. 


