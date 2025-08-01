# AI-Automated Aspen Project

This project integrates Aspen Plus software with LLMs and RAG (Retrieval-Augmented Generation) technology for automated simulation, carbon emission analysis, and literature research.

## Requirements

- Python 3.8+ (for LangChain and RAG integration)
- Windows OS (for Aspen Plus integration)
- Aspen Plus software installed
- Docker (for MCP tools, optional)
- API keys for various services

## Quick Start

### 1. Python Environment Setup

```bash
# Clone the repository
git clone <repository-url>
cd code_absolute_readme

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the project root:

```env
LLAMA_API_KEY=your_llama_parse_api_key
LLM_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### 3. Directory Setup

Create necessary directories:

```bash
mkdir bkp_all inp_outputs carbon_papers parsed_docs db_carbon_papers
```

## Usage

### Module 1: MCP Download (BKP Files)

*Note: Detailed documentation for MCP download module is available in the existing README.*

The MCP (Model Context Protocol) module downloads BKP files from various sources for use as learning materials.

**Files Used:**
- `AI-automated-Aspen-main/` - MCP configuration and tools
- `configs/mcp_config.json` - MCP server configuration
- `src/data_collection_github_agent/` - GitHub data collection agent
- `scripts/create_download_list.py` - Download list generation

### Module 2: Aspen File Generation

Generate comprehensive Aspen Plus simulation files using downloaded BKP files as learning materials.

**Core Files:**
- `inp_generate/run_all.py` - Main execution script (all-in-one)
- `inp_generate/bkp-inp-update.py` - BKP to INP conversion
- `inp_generate/traditional_distillation_inp.py` - Traditional distillation models
- `inp_generate/optimized_condition.py` - Optimal parameter application
- `inp_generate/traditional_carbon_accounting.py` - Carbon emission calculation
- `inp_generate/image_rr.py` - Reflux ratio sensitivity analysis
- `inp_generate/image_duty.py` - Heat duty sensitivity analysis
- `inp_generate/heatpump_distillation_inp.py` - Heat pump distillation models
- `inp_generate/heatpump_carbon_accounting.py` - Heat pump carbon emissions
- `inp_generate/image_carbon_emissions.py` - Carbon emissions comparison

**Supporting Directories and Files:**
- `input_guide/` - Aspen Plus input guide files
  - `15 Rigorous Distillation_RADFRAC.md` - RadFrac model guide
  - `30 Design Specifications.md` - Design specification guide
  - `35 Sensitivity Blocks.md` - Sensitivity analysis guide
- `inp_outputs/` - Learning files directory (contains example .inp files)
- `bkp_all/` - BKP files for conversion
- `inp_generate/simple/` - Output directory for generated files
- `inp_generate/difficult/` - Advanced model output directory
- `selected_files/` - Classified and organized learning files
  - `dstwu_models/` - DSTWU shortcut model files
  - `radfrac_models/` - RadFrac rigorous model files
  - `radfrac_keyword_models/` - Files with RADFRAC keyword
  - `sensitivity_keyword_models/` - Files with SENSITIVITY keyword
  - `design_spec_keyword_models/` - Files with DESIGN-SPEC keyword
  - `excluded_large_files/` - Large files (>20KB)

#### Quick Start (All-in-One)
```bash
python inp_generate/run_all.py
```

#### Step-by-Step Execution
```bash
# Convert BKP to INP format
python inp_generate/bkp-inp-update.py

# Generate traditional distillation models
python inp_generate/traditional_distillation_inp.py

# Apply optimal conditions
python inp_generate/optimized_condition.py

# Calculate carbon emissions
python inp_generate/traditional_carbon_accounting.py

# Generate sensitivity analysis charts
python inp_generate/image_rr.py
python inp_generate/image_duty.py

# Generate heat pump models
python inp_generate/heatpump_distillation_inp.py

# Calculate heat pump carbon emissions
python inp_generate/heatpump_carbon_accounting.py

# Generate comparison charts
python inp_generate/image_carbon_emissions.py
```

### Module 3: RAG Literature Research

Download and analyze 100+ carbon emission factor papers using RAG technology.

**Core Files:**
- `downloader/search.py` - Multi-source paper search (ArXiv, Crossref, Unpaywall)
- `downloader/download.py` - Batch paper downloading
- `downloader/metadata.py` - Metadata export and deduplication
- `downloader/standards.py` - Carbon emission standards download
- `downloader/utils.py` - Utility functions and logging
- `downloader/__init__.py` - Package initialization

**Supporting Directories:**
- `carbon_papers/` - Downloaded research papers
- `parsed_docs/` - Parsed markdown files from papers
- `db_carbon_papers/` - Vector database for RAG queries

```bash
# Configure search parameters
python downloader/search.py

# Download papers
python downloader/download.py

# Export metadata
python downloader/metadata.py

# Download standards
python downloader/standards.py
```

### Module 4: Cooling Tower Analysis

Extract and analyze cooling tower fan power data using RAG technology.

**Core Files:**
- `rag_table/main_table.py` - Main table processing script
- `rag_table/gxt_rag.py` - Cooling tower data query system
- `rag_table/download_images.py` - Specification image downloader
- `rag_table/config_table.py` - Table-specific configuration
- `rag_table/parsing_table.py` - Table parsing utilities
- `rag_table/vectordb_table.py` - Vector database for table data
- `rag_table/qa_chain_table.py` - Q&A chain for table queries
- `rag_table/process_table.py` - Table processing utilities

**Supporting Directories and Files:**
- `rag_table/parsed_Web_PDF/` - Parsed web PDF content
  - `gxt_specification_table_parsed.md` - Cooling tower specification table
- `rag_table/web_content/` - Web scraped images
  - `gxt_spec_table_part1.jpg` - Specification table part 1
  - `gxt_spec_table_part2.jpg` - Specification table part 2
- `rag_table/db_Web_PDF/` - Vector database for web PDF content

```bash
# Process cooling tower specifications
python rag_table/main_table.py --action=parse

# Query cooling tower data
python rag_table/gxt_rag.py

# Download specification images
python rag_table/download_images.py
```

## Complete Workflow

### 1. Literature Research Phase
```bash
# Uses: downloader/search.py, downloader/download.py
# Outputs to: carbon_papers/, parsed_docs/, db_carbon_papers/
python downloader/search.py
python downloader/download.py
```

### 2. Aspen Simulation Phase
```bash
# Uses: inp_generate/run_all.py, input_guide/, inp_outputs/, bkp_all/
# Outputs to: inp_generate/simple/, inp_generate/difficult/, selected_files/
python inp_generate/run_all.py
```

### 3. Analysis Phase
```bash
# Uses: rag_table/gxt_rag.py, rag_table/parsed_Web_PDF/
# Uses: inp_generate/traditional_carbon_accounting.py
python rag_table/gxt_rag.py
python inp_generate/traditional_carbon_accounting.py
```

## Output Files

### Simulation Files
- `*.inp` - Aspen Plus input files
- `*.bkp` - Simulation backup files
- `*.rep` - Simulation reports

### Analysis Charts
- `reflux_ratio_analysis.html` - Reflux ratio sensitivity
- `heat_duty_analysis.html` - Heat duty sensitivity
- `carbon_emissions_comparison.html` - Carbon footprint comparison

### Literature Files
- `papers_metadata.csv` - Paper metadata
- `carbon_standards_metadata.csv` - Standards metadata
- `*.pdf` - Downloaded research papers

### Reports
- `carbon_emission_analysis.docx` - Carbon emission report
- `heat_pump_analysis.docx` - Heat pump analysis

## Troubleshooting

### Common Issues

1. **Dependency Installation Issues**
   - Ensure Python 3.8+ is installed
   - Verify virtual environment is activated
   - Check pip is up to date: `pip install --upgrade pip`
   - If installation fails, try: `pip install -r requirements.txt --force-reinstall`

2. **Aspen Plus Integration**
   - Ensure Aspen Plus is properly installed
   - Check Windows COM interface
   - Verify pywin32 installation

3. **API Key Issues**
   - Verify all API keys in `.env`
   - Check API service status
   - Monitor API usage limits

4. **Memory Issues**
   - Use minimal requirements for large datasets
   - Increase system memory if needed
   - Process files in smaller batches

## Project Structure

```
code_absolute_readme/
├── AI-automated-Aspen-main/     # MCP tools and configuration
│   ├── configs/mcp_config.json  # MCP server configuration
│   ├── src/data_collection_github_agent/  # GitHub data collection
│   └── scripts/create_download_list.py    # Download list generation
├── bkp_all/                    # BKP files for learning
├── inp_outputs/               # Learning files directory (.inp files)
├── carbon_papers/             # Carbon emission literature
├── parsed_docs/              # Parsed markdown files
├── db_carbon_papers/         # Vector database for literature
├── input_guide/              # Aspen Plus input guides
│   ├── 15 Rigorous Distillation_RADFRAC.md
│   ├── 30 Design Specifications.md
│   └── 35 Sensitivity Blocks.md
├── rag_modular/              # RAG system modules
│   ├── main.py               # Main RAG execution
│   ├── config.py             # RAG configuration
│   ├── parsing.py            # PDF parsing utilities
│   ├── vectordb.py           # Vector database operations
│   ├── qa_chain.py           # Q&A chain setup
│   └── utils.py              # RAG utilities
├── rag_table/                # Table-specific RAG
│   ├── main_table.py         # Table processing main script
│   ├── gxt_rag.py            # Cooling tower data query
│   ├── config_table.py       # Table-specific configuration
│   ├── parsing_table.py      # Table parsing utilities
│   ├── vectordb_table.py     # Table vector database
│   ├── qa_chain_table.py     # Table Q&A chain
│   ├── process_table.py      # Table processing utilities
│   ├── download_images.py    # Image downloader
│   ├── parsed_Web_PDF/       # Parsed web PDF content
│   ├── web_content/          # Web scraped images
│   └── db_Web_PDF/           # Vector database for web PDF
├── downloader/               # Literature downloader
│   ├── search.py             # Multi-source paper search
│   ├── download.py           # Batch paper downloading
│   ├── metadata.py           # Metadata export
│   ├── standards.py          # Standards download
│   ├── utils.py              # Utility functions
│   └── __init__.py           # Package initialization
├── inp_generate/            # Aspen file generation
│   ├── run_all.py           # Main execution script
│   ├── bkp-inp-update.py    # BKP to INP conversion
│   ├── traditional_distillation_inp.py  # Traditional models
│   ├── optimized_condition.py           # Optimal parameters
│   ├── traditional_carbon_accounting.py # Carbon emissions
│   ├── image_rr.py          # Reflux ratio analysis
│   ├── image_duty.py        # Heat duty analysis
│   ├── heatpump_distillation_inp.py    # Heat pump models
│   ├── heatpump_carbon_accounting.py   # Heat pump emissions
│   ├── image_carbon_emissions.py       # Emissions comparison
│   ├── simple/              # Output directory for basic models
│   └── difficult/           # Output directory for advanced models
├── selected_files/          # Classified learning files
│   ├── dstwu_models/        # DSTWU shortcut model files
│   ├── radfrac_models/      # RadFrac rigorous model files
│   ├── radfrac_keyword_models/     # Files with RADFRAC keyword
│   ├── sensitivity_keyword_models/  # Files with SENSITIVITY keyword
│   ├── design_spec_keyword_models/  # Files with DESIGN-SPEC keyword
│   └── excluded_large_files/       # Large files (>20KB)
├── requirements.txt         # Python dependencies
└── README.md               # This documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review module-specific documentation
- Open an issue on the repository

---

**Note**: This project integrates multiple AI technologies to automate the entire workflow from literature research to simulation analysis. Each module can be used independently or as part of the complete pipeline. 