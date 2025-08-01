import asyncio
import re
import numpy as np
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.chains import RetrievalQA
from tqdm import tqdm

# Import configuration
from config import MD_DIR, QWEN_API_KEY, QWEN_BASE_URL

def extract_natural_gas_values(text):
    """Function specifically for extracting natural gas emission factors"""
    # New: Match table format data
    table_pattern = r'\|\s*Natural\s+Gas\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)\s*\|'
    table_match = re.search(table_pattern, text, re.IGNORECASE)
    
    if table_match:
        default = table_match.group(1).replace(',', '')
        lower = table_match.group(2).replace(',', '')
        upper = table_match.group(3).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # New: Match list format "**Default**: 56,100" "**Lower**: 54,300" "**Upper**: 58,300"
    list_default_match = re.search(r'\*\*Default.*?\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    list_lower_match = re.search(r'\*\*Lower.*?\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    list_upper_match = re.search(r'\*\*Upper.*?\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    
    if list_default_match and list_lower_match and list_upper_match:
        default = list_default_match.group(1).replace(',', '')
        lower = list_lower_match.group(1).replace(',', '')
        upper = list_upper_match.group(1).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # New: Match RAG returned format "**CO₂ Default Emission Factor**: 56,100 kg CO₂/TJ"
    rag_default_match = re.search(r'\*\*CO₂\s+Default\s+Emission\s+Factor\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    rag_lower_match = re.search(r'\*\*CO₂\s+Lower\s+Emission\s+Factor\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    rag_upper_match = re.search(r'\*\*CO₂\s+Upper\s+Emission\s+Factor\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    
    if rag_default_match and rag_lower_match and rag_upper_match:
        default = rag_default_match.group(1).replace(',', '')
        lower = rag_lower_match.group(1).replace(',', '')
        upper = rag_upper_match.group(1).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # Strategy 1: Match Natural Gas row in various formats
    gas_patterns = [
        r'\|\s*Natural\s+Gas\s*\|\s*([0-9,]+)\s*\|',
        r'Natural\s+Gas[^\d]*([0-9,]+)',
        r'\*\*Natural\s+Gas\*\*[^\d]*([0-9,]+)',
        r'Natural\s+Gas\s*\|\s*([0-9,]+)\s*\|',
        r'Natural\s+Gas[^|]*\|\s*([0-9,]+)'
    ]
    
    for pattern in gas_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).replace(',', '')
            if value and value.isdigit() and int(value) > 10000:
                default = value
                unit = "kgCO₂/TJ"
                
                # Try to extract upper and lower bounds
                # 1. Match "lower uncertainty range is X...upper uncertainty range is Y" format
                uncertainty_pattern = r'lower\s+uncertainty\s+range\s+is\s*([0-9,]+).*?upper\s+uncertainty\s+range\s+is\s*([0-9,]+)'
                uncertainty_match = re.search(uncertainty_pattern, text, re.IGNORECASE | re.DOTALL)
                
                if uncertainty_match:
                    lower = uncertainty_match.group(1).replace(',', '')
                    upper = uncertainty_match.group(2).replace(',', '')
                    return default, unit, lower, upper
                
                # 2. Match regular bound format
                lower_match = re.search(r'lower\s+bound.*?([0-9,]+)', text, re.IGNORECASE)
                upper_match = re.search(r'upper\s+bound.*?([0-9,]+)', text, re.IGNORECASE)
                
                if lower_match and upper_match:
                    lower = lower_match.group(1).replace(',', '')
                    upper = upper_match.group(1).replace(',', '')
                    return default, unit, lower, upper
                
                return default, unit, "[Need to query upper and lower bounds]", "[Need to query upper and lower bounds]"
    
    return "[Unable to extract default value]", "[Unable to extract unit]", "[Unable to extract lower limit]", "[Unable to extract upper limit]"

def extract_lignite_values(text):
    """Function specifically for extracting lignite emission factors"""
    # New: Match table format data - fixed format matching
    table_pattern = r'\|\s*Lignite\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)–([0-9,]+)\s*\|'
    table_match = re.search(table_pattern, text, re.IGNORECASE)
    
    if table_match:
        default = table_match.group(1).replace(',', '')
        lower = table_match.group(2).replace(',', '')
        upper = table_match.group(3).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # New: Match table format data - another format
    table_pattern2 = r'\|\s*Lignite\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)\s*–\s*([0-9,]+)\s*\|'
    table_match2 = re.search(table_pattern2, text, re.IGNORECASE)
    
    if table_match2:
        default = table_match2.group(1).replace(',', '')
        lower = table_match2.group(2).replace(',', '')
        upper = table_match2.group(3).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # New: Match table format data - three-column format
    table_pattern3 = r'\|\s*Lignite\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)\s*\|\s*([0-9,]+)\s*\|'
    table_match3 = re.search(table_pattern3, text, re.IGNORECASE)
    
    if table_match3:
        default = table_match3.group(1).replace(',', '')
        lower = table_match3.group(2).replace(',', '')
        upper = table_match3.group(3).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # New: Match new data format "**Lower Heating Value**: 101,000 MJ/t" "**Carbon Content**: 90,900 kg C/t" "**Emission Factor (CO₂)**: 115,000 kg CO₂/t"
    heating_value_match = re.search(r'\*\*Lower\s+Heating\s+Value\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    carbon_content_match = re.search(r'\*\*Carbon\s+Content\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    emission_factor_match = re.search(r'\*\*Emission\s+Factor\s*\(CO₂\)\*\*.*?:\s*([0-9,]+)', text, re.IGNORECASE)
    
    if heating_value_match and carbon_content_match and emission_factor_match:
        default = heating_value_match.group(1).replace(',', '')
        lower = carbon_content_match.group(1).replace(',', '')
        upper = emission_factor_match.group(1).replace(',', '')
        return default, "kgCO₂/TJ", lower, upper
    
    # Strategy 1: Match Lignite row in various formats, prioritize Lignite over other Coal
    lignite_patterns = [
        r'\|\s*Lignite\s*\|\s*([0-9,]+)\s*\|',
        r'Lignite[^\d]*([0-9,]+)\s*kg',
        r'\*\*Lignite[^:]*:\s*([0-9,]+)',
        r'lignite[^0-9]*emission\s+factor[^0-9]*([0-9,]+)',
        r'Net\s+calorific\s+value:\s*([0-9,]+)\s*TJ',
        r'Lignite[^:]*:\s*.*?([0-9,]+)\s*TJ'
    ]
    
    for pattern in lignite_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).replace(',', '')
            if value and value.isdigit() and int(value) > 10000:
                default = value
                unit = "kgCO₂/TJ"
                
                # Try to extract upper and lower bounds - various formats
                # 1. Match "lower bound of X and an upper bound of Y" format
                bound_of_pattern = r'lower\s+bound\s+of\s*([0-9,]+).*?an?\s*upper\s+bound\s+of\s*([0-9,]+)'
                bound_of_match = re.search(bound_of_pattern, text, re.IGNORECASE | re.DOTALL)
                
                if bound_of_match:
                    lower = bound_of_match.group(1).replace(',', '')
                    upper = bound_of_match.group(2).replace(',', '')
                    return default, unit, lower, upper
                
                # 2. Match list format "Lower bound: 90,900" "Upper bound: 115,000"
                list_lower_match = re.search(r'Lower\s+bound.*?:\s*([0-9,]+)', text, re.IGNORECASE)
                list_upper_match = re.search(r'Upper\s+bound.*?:\s*([0-9,]+)', text, re.IGNORECASE)
                
                # 3. Match "Mid value" as default value
                mid_value_match = re.search(r'Mid\s+value.*?:\s*([0-9,]+)', text, re.IGNORECASE)
                
                if list_lower_match and list_upper_match and mid_value_match:
                    lower = list_lower_match.group(1).replace(',', '')
                    upper = list_upper_match.group(1).replace(',', '')
                    default = mid_value_match.group(1).replace(',', '')
                    return default, unit, lower, upper
                
                if list_lower_match and list_upper_match:
                    lower = list_lower_match.group(1).replace(',', '')
                    upper = list_upper_match.group(1).replace(',', '')
                    return default, unit, lower, upper
                
                # 3. Match "upper and lower bounds...are X and Y, respectively" format (upper bound first)
                upper_lower_pattern = r'upper\s+and\s+lower\s+bounds.*?are\s*\*?\*?([0-9,]+).*?and\s*\*?\*?([0-9,]+)'
                upper_lower_match = re.search(upper_lower_pattern, text, re.IGNORECASE | re.DOTALL)
                
                if upper_lower_match:
                    upper = upper_lower_match.group(1).replace(',', '')
                    lower = upper_lower_match.group(2).replace(',', '')
                    return default, unit, lower, upper
                
                # 4. Match "lower and upper bounds...are X and Y, respectively" format (lower bound first)
                bounds_pattern = r'lower\s+and\s+upper\s+bounds.*?are\s*\*?\*?([0-9,]+).*?and\s*\*?\*?([0-9,]+)'
                bounds_match = re.search(bounds_pattern, text, re.IGNORECASE | re.DOTALL)
                
                if bounds_match:
                    lower = bounds_match.group(1).replace(',', '')
                    upper = bounds_match.group(2).replace(',', '')
                    return default, unit, lower, upper
                
                return default, unit, "[Need to query upper and lower bounds]", "[Need to query upper and lower bounds]"
    
    # Strategy 2: If Lignite not found, search for general Coal
    coal_patterns = [
        r'\|\s*Coal\s*\|\s*([0-9,]+)\s*\|',
        r'Coal[^\d]*([0-9,]+)\s*kg'
    ]
    for pattern in coal_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).replace(',', '')
            if value and value.isdigit() and int(value) > 10000:
                default = value
                unit = "kgCO₂/TJ"
                return default, unit, "[Need to query upper and lower bounds]", "[Need to query upper and lower bounds]"
    
    return "[Unable to extract default value]", "[Unable to extract unit]", "[Unable to extract lower limit]", "[Unable to extract upper limit]"

def extract_coal_gas_values(text, fuel_name):
    """Unified interface function, calls specific fuel processing functions"""
    if 'natural gas' in fuel_name.lower() or 'gas' in fuel_name.lower():
        return extract_natural_gas_values(text)
    elif 'lignite' in fuel_name.lower() or 'coal' in fuel_name.lower():
        return extract_lignite_values(text)
    else:
        return "[Unable to extract default value]", "[Unable to extract unit]", "[Unable to extract lower limit]", "[Unable to extract upper limit]"

def get_formatted_coal_gas_factors(fuel_name, response_text, output_label=None):
    default, unit, lower, upper = extract_coal_gas_values(response_text, fuel_name)
    label = output_label if output_label else fuel_name
    return f"{label}: {default} {unit} ({lower}, {upper})"

def process_biomass_response(response_text):
    """Process biomass response, dynamically extract Carbon Dioxide Emissions values from tables"""
    
    # Method 1: Extract Per MWh column values from RAG returned table format
    # Match format: | Biomass Type | Per ODT | Per MWh |
    #           | Whole tree thinnings | 94.34 | 28.07 |
    table_pattern = r'\|\s*[^|]*\s*\|\s*[0-9,.]+\s*\|\s*([0-9,]+\.?[0-9]*)\s*\|'
    matches = re.findall(table_pattern, response_text)
    
    values = []
    for match in matches:
        try:
            val = float(match.replace(',', ''))
            # Filter out obviously unreasonable values (e.g., 0 or very large values)
            if 0 < val < 100:  # Reasonable kg CO₂/MWh range
                values.append(val)
        except ValueError:
            continue
    
    # Method 2: If table matching fails, try to search for numbers containing "kg CO₂"
    if not values:
        # Search for numbers in kg CO₂ format
        kg_co2_pattern = r'(\d+\.?\d*)\s*kg\s*CO[₂2]'
        matches = re.findall(kg_co2_pattern, response_text, re.IGNORECASE)
        
        for match in matches:
            try:
                val = float(match)
                if 0 < val < 100:  # Reasonable range
                    values.append(val)
            except ValueError:
                continue
    
    # Method 3: Search for numbers in tables, especially the Carbon Dioxide Emissions column
    if not values:
        # More lenient table matching pattern
        # Match table rows containing numbers
        table_row_pattern = r'\|\s*[^|]*\|\s*([0-9,]+\.?[0-9]*)\s*\|'
        matches = re.findall(table_row_pattern, response_text)
        
        for match in matches:
            try:
                val = float(match.replace(',', ''))
                if 0 < val < 100:  # Reasonable range
                    values.append(val)
            except ValueError:
                continue
    
    # Deduplicate and sort
    values = sorted(list(set(values)))
    
    # If values are found, calculate statistics
    if values:
        min_val = min(values)
        max_val = max(values)
        
        # Calculate average (excluding one max and one min)
        if len(values) <= 2:
            avg = sum(values) / len(values)
        else:
            # Calculate average after removing max and min
            filtered_values = sorted(values)[1:-1]
            if not filtered_values:
                avg = sum(values) / len(values)
            else:
                avg = sum(filtered_values) / len(filtered_values)
        
        units = "kg CO₂/MWh"
        result_txt = f"Biomass: {avg:.2f} {units} ({min_val:.2f}-{max_val:.2f})"
        return result_txt
    
    return "Biomass: Unable to find or parse target table from response (cannot calculate)"

async def load_markdown_files(md_files):
    """Asynchronously load all Markdown files"""
    documents = []
    for md_file in tqdm(md_files, desc="Loading Markdown files"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            doc = Document(page_content=content, metadata={"source": str(md_file)})
            documents.append(doc)
        except Exception as e:
            print(f"Error loading file {md_file}: {e}")
    return documents

async def create_faiss_vectordb(documents, embeddings):
    """Asynchronously create FAISS vector database"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,  # Adjust to DashScope limit
        chunk_overlap=300,
    )
    texts = text_splitter.split_documents(documents)
    
    if not texts:
        raise ValueError("No text chunks could be extracted from documents.")
    
    loop = asyncio.get_event_loop()
    vectordb = await loop.run_in_executor(None, FAISS.from_documents, texts, embeddings)
    return vectordb

# --- RAG Initialization and Components ---
async def initialize_rag_components():
    """Initialize all components of the RAG system (DashScope + FAISS)."""
    # 1. Use DashScope Embeddings
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v2",
        dashscope_api_key="<your api key>"
    )
    
    # 2. Use Qwen LLM
    llm = ChatOpenAI(
        model_name="<your model>",
        temperature=0,
        openai_api_key="<your api key>",
        base_url=QWEN_BASE_URL
    )
    
    # 3. Load documents
    md_dir_path = Path(MD_DIR)
    if not md_dir_path.exists() or not any(md_dir_path.glob("*_parsed.md")):
        raise ValueError(f"Markdown directory '{MD_DIR}' does not exist or is empty.")
    
    md_files = list(md_dir_path.glob("*_parsed.md"))
    documents = await load_markdown_files(md_files)
    
    # 4. Create FAISS vector database
    vectordb = await create_faiss_vectordb(documents, embeddings)
    
    # 5. Set up question-answering chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(search_kwargs={"k": 80}),  # Increase retrieval quantity
        return_source_documents=True
    )
    
    return qa_chain

# --- RAG Query Function ---
async def run_single_query(qa_chain, query_text):
    """Asynchronously execute a single query and return the result and source documents"""
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None, 
        lambda: qa_chain({"query": query_text})
    )
    return result['result'], result['source_documents']

async def get_coal_gas_from_rag(qa_chain):
    """Query coal and natural gas emission factors using the RAG chain."""
    # Query coal and natural gas emission factors
    lignite_query = "Show me the emission factor table for Lignite"
    natural_gas_query = "What is the exact value of CO₂ Default, Lower, Upper EMISSION FACTORS for Natural Gas in stationary combustion tables"
    formatted_results = []
    
    # Get query results and source documents
    lignite_result, natural_gas_result = await asyncio.gather(
        run_single_query(qa_chain, lignite_query),
        run_single_query(qa_chain, natural_gas_query)
    )
    
    lignite_result_text, lignite_sources = lignite_result
    natural_gas_result_text, natural_gas_sources = natural_gas_result
    
    # Process coal and natural gas results
    formatted_results.append(get_formatted_coal_gas_factors("Lignite", lignite_result_text, "Coal"))
    formatted_results.append(get_formatted_coal_gas_factors("Natural Gas", natural_gas_result_text))

    return formatted_results

async def get_biomass_from_rag(qa_chain):
    """Query biomass emission factors using the RAG chain."""
    biomass_query = "Show me the complete table with Carbon Dioxide Emissions (kg CO2, per MWh) for four biomass types"
    
    # Update to return tuple format
    biomass_result_text, _ = await run_single_query(qa_chain, biomass_query)
    
    formatted_result = process_biomass_response(biomass_result_text)

    return formatted_result

# --- Main Execution Logic ---
async def run_query_steam_factors():
    """Initialize RAG, run queries, and return a formatted list of results (with '- ' prefix)."""
    qa_chain = await initialize_rag_components()

    # Execute coal/gas and biomass queries in parallel
    results_tasks = await asyncio.gather(
        get_coal_gas_from_rag(qa_chain),
        get_biomass_from_rag(qa_chain)
    )

    coal_gas_results, biomass_result = results_tasks

    # Combine raw results
    raw_results = coal_gas_results + [biomass_result]

    # Format results list, add '- ' prefix
    formatted_results = [f"- {result}" for result in raw_results]

    # Return formatted list
    return formatted_results


if __name__ == "__main__":
    results = asyncio.run(run_query_steam_factors())
    print("\nSteam fuel emission factors:")
    for line in results:
        print(line)