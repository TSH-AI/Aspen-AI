"""
power_range_rag_local.py
Final stable version: Combining domestic DashScope API and local FAISS vector database
"""

import asyncio
import re
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.chains import RetrievalQA
from tqdm import tqdm

from config import MD_DIR, QWEN_API_KEY, QWEN_BASE_URL

def extract_emission_factor(text, technology):
    """Extract emission factors from text, supporting LaTeX mathematical symbol format"""
    
    # Function to clean LaTeX mathematical symbols
    def clean_latex_math(text):
        """Convert LaTeX mathematical symbols to plain text"""
        # Handle common LaTeX mathematical symbols
        text = re.sub(r'\$([^$]*)\$', r'\1', text)  # Remove $ symbols
        text = re.sub(r'\\mathsf\s*\{\s*([^}]*)\s*\}', r'\1', text)  # Remove \mathsf{}
        text = re.sub(r'\\mathfrak\s*\{\s*([^}]*)\s*\}', r'\1', text)  # Remove \mathfrak{}
        text = re.sub(r'\\sf\s*([a-zA-Z])', r'\1', text)  # Remove \sf
        text = re.sub(r'\\thinspace', ' ', text)  # Remove \thinspace
        text = re.sub(r'\\operatorname\s*\{\s*([^}]*)\s*\}', r'\1', text)  # Remove \operatorname{}
        text = re.sub(r'_\s*\{\s*([^}]*)\s*\}', r'_\1', text)  # Simplify subscripts
        text = re.sub(r'\^\s*\{\s*([^}]*)\s*\}', r'^\1', text)  # Simplify superscripts
        text = re.sub(r'~', ' ', text)  # Replace tilde with space
        text = re.sub(r'\s+', ' ', text)  # Merge multiple spaces
        return text.strip()
    
    # Clean input text
    cleaned_text = clean_latex_math(text)
    
    print(f"\n=== Extracting {technology} emission factors ===")
    print(f"Original text length: {len(text)}")
    print(f"Cleaned text fragment: {cleaned_text[:500]}...")
    

    
    # Technology keyword mapping
    tech_patterns = {
        'coal': ['coal'],
        'gas': ['gas', 'natural gas'],
        'wind': ['wind']
    }
    
    # More powerful numerical extraction patterns
    patterns = [
        # "from X to Y" format (add this first for priority)
        r'from\s+(\d+(?:\.\d+)?)\s+to\s+(\d+(?:\.\d+)?)\s*(?:g\s*CO\s*2\s*eq|gCO2eq|gCO₂eq)/?(?:k?Wh)?',
        # LaTeX math format: $710 - 950\text{gCO}_2\text{eq} /\text{kWh}$
        r'(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*\\text\s*\{\s*gCO\s*\}\s*_\s*2\s*\\text\s*\{\s*eq\s*\}\s*/\s*\\text\s*\{\s*kWh\s*\}',
        # Standard format: XX.X - YY.Y
        r'(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*(?:g\s*CO\s*2\s*eq|gCO2eq|gCO₂eq)/?(?:k?Wh)?',
        # LaTeX cleaned format: XX – YY gCO 2 eq/kWh
        r'(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*g\s*CO\s*2?\s*eq\s*/?\s*k?\s*Wh?',
        # More flexible format
        r'(\d+(?:\.\d+)?)\s*[-–—]\s*(\d+(?:\.\d+)?)\s*(?:gCO2|g\s*CO\s*2)',
        # Single value format
        r'(\d+(?:\.\d+)?)\s*(?:g\s*CO\s*2\s*eq|gCO2eq|gCO₂eq)/?(?:k?Wh)?'
    ]
    
    # Find technology-related content
    tech_keywords = tech_patterns.get(technology.lower(), [technology.lower()])
    
    # Search for technology-specific numerical ranges
    lines = cleaned_text.split('\n')
    
    if technology.lower() == 'gas':
        # For gas, find lines that mention gas but exclude lines that also mention coal
        relevant_lines = []
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in tech_keywords):
                # Make sure this line doesn't also contain coal-related keywords
                if not any(coal_word in line_lower for coal_word in ['coal', 'hard coal']):
                    relevant_lines.append(line)
        
        # If we found gas-specific lines, use them; otherwise fallback to full text
        if relevant_lines:
            relevant_text = '\n'.join(relevant_lines)
        else:
            relevant_text = cleaned_text
    else:
        # For other technologies, use standard approach
        relevant_lines = []
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in tech_keywords):
                relevant_lines.append(line)
        
        if relevant_lines:
            relevant_text = '\n'.join(relevant_lines)
        else:
            relevant_text = cleaned_text
    print(f"Relevant text fragment: {relevant_text[:300]}...")
    
    # Try each pattern
    for pattern_idx, pattern in enumerate(patterns):
        print(f"\nTrying pattern {pattern_idx + 1}: {pattern}")
        
        matches = re.finditer(pattern, relevant_text, re.IGNORECASE)
        for match in matches:
            print(f"Found match: {match.group()}")
            print(f"Match context: {relevant_text[max(0, match.start()-50):match.end()+50]}")
            
            if len(match.groups()) >= 2:
                min_val = float(match.group(1))
                max_val = float(match.group(2))
                avg_val = (min_val + max_val) / 2
                
                print(f"✅ Successfully extracted: min={min_val}, max={max_val}, avg={avg_val}")
                return {
                    'min': min_val,
                    'max': max_val,
                    'average': avg_val,
                    'range': f"{min_val}-{max_val}",
                    'unit': 'gCO₂eq/kWh'
                }
            elif len(match.groups()) >= 1:
                val = float(match.group(1))
                print(f"✅ Successfully extracted single value: {val}")
                return {
                    'min': val,
                    'max': val,
                    'average': val,
                    'range': str(val),
                    'unit': 'gCO₂eq/kWh'
                }
    
    print(f"❌ Failed to extract {technology} emission factors")
    return None

def extract_wind_power_range_and_average(response_text):
    """
    Return format: {'min': float, 'max': float, 'avg': float, 'unit': str}
    """
    wind_data = {'min': None, 'max': None, 'avg': None, 'unit': 'gCO₂eq/kWh'}
    wind_range_pattern = r"(\d+)\s*[–-]\s*(\d+)\s*(g[^0-9\s]*(?:CO₂|CO2)(?:eq)?\/kWh)"
    match = re.search(wind_range_pattern, response_text, re.IGNORECASE)
    
    if match:
        try:
            min_val = float(match.group(1))
            max_val = float(match.group(2))
            avg_val = (min_val + max_val) / 2
            unit = match.group(3)
            
            wind_data = {
                'min': min_val,
                'max': max_val,
                'avg': avg_val,
                'unit': unit
            }
        except (ValueError, IndexError) as e:
            print(f"Error extracting wind power values: {e}")
    
    return wind_data

def extract_coal_gas_range_and_average(response_text):
    results = {
        'coal': {'min': None, 'max': None, 'avg': None, 'unit': 'gCO₂eq/kWh'},
        'gas': {'min': None, 'max': None, 'avg': None, 'unit': 'gCO₂eq/kWh'}
    }
    
    # More robust parsing logic: process line by line
    lines = response_text.split('\n')
    range_pattern = r"(\d+)\s*[–-]\s*(\d+)\s*(gCO₂eq\s?/\s?kWh)"

    for line in lines:
        if 'coal' in line.lower():
            match = re.search(range_pattern, line, re.IGNORECASE)
            if match:
                try:
                    min_val = float(match.group(1))
                    max_val = float(match.group(2))
                    results['coal'] = {
                        'min': min_val,
                        'max': max_val,
                        'avg': (min_val + max_val) / 2,
                        'unit': 'gCO₂eq/kWh'
                    }
                except (ValueError, IndexError) as e:
                    print(f"Error extracting coal values: {e}")
        
        if 'gas' in line.lower():
            match = re.search(range_pattern, line, re.IGNORECASE)
            if match:
                try:
                    min_val = float(match.group(1))
                    max_val = float(match.group(2))
                    results['gas'] = {
                        'min': min_val,
                        'max': max_val,
                        'avg': (min_val + max_val) / 2,
                        'unit': 'gCO₂eq/kWh'
                    }
                except (ValueError, IndexError) as e:
                    print(f"Error extracting gas values: {e}")
            
    return results

def format_emission_factor_result(fuel_name, data):
    if data and data.get('min') is not None and data.get('max') is not None:
        avg = data.get('avg') or data.get('average')  # Support both key names
        if avg is not None:
            unit = data.get('unit', 'gCO₂eq/kWh')
            return f"{fuel_name}: {avg:.1f} {unit} ({data['min']:.1f}-{data['max']:.1f})"
    return f"{fuel_name}: Data extraction failed"

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
        chunk_size=1024,
        chunk_overlap=200,
    )
    texts = text_splitter.split_documents(documents)
    print(f"Documents split into {len(texts)} text chunks")
    
    if not texts:
        raise ValueError("Failed to extract any text chunks from documents.")
    
    print("Creating FAISS vector database...")
    # FAISS.from_documents is a synchronous operation, but can be called this way in async function
    vectordb = await asyncio.to_thread(FAISS.from_documents, texts, embeddings)
    print("FAISS vector database creation completed!")
    return vectordb

async def initialize_rag_components():
    """Initialize all components of the RAG system"""
    print("Initializing RAG system (DashScope + FAISS)...")
    
    # 1. Use DashScope Embeddings (with direct API key to avoid cache issues)
    embeddings = DashScopeEmbeddings(
        model="text-embedding-v2",
        dashscope_api_key="<your api key>"
    )
    
    # 2. Use Qwen LLM (with direct API key to avoid cache issues)
    llm = ChatOpenAI(
        model_name="<your model>",
        temperature=0,
        openai_api_key="<your api key>",
        base_url=QWEN_BASE_URL
    )
    
    # 3. Load documents
    # Make MD_DIR path relative to the script location
    script_dir = Path(__file__).parent
    md_dir_path = script_dir / MD_DIR
    if not md_dir_path.exists() or not any(md_dir_path.glob("*_parsed.md")):
        raise ValueError(f"Markdown directory '{md_dir_path}' does not exist or is empty.")
    
    md_files = list(md_dir_path.glob("*_parsed.md"))
    documents = await load_markdown_files(md_files)
    
    # 4. Create FAISS vector database
    vectordb = await create_faiss_vectordb(documents, embeddings)
    
    # 5. Set up QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(search_kwargs={"k": 15}), # Increase k value for more comprehensive context
        return_source_documents=True
    )
    
    print("RAG system initialization completed.")
    return qa_chain

async def run_single_query(qa_chain, query_text):
    """Asynchronously execute a single query"""
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None, 
        lambda: qa_chain({"query": query_text})
    )
    return result['result']

async def get_power_range_from_rag():
    qa_chain = await initialize_rag_components()
    
    coal_query = "From AR5, based on the revised assessment of fugitive methane emissions, what are the carbon emission factors for modern hard coal power plants? Please provide the range and average."
    gas_query = "From AR5, based on the revised assessment of fugitive methane emissions, what are the carbon emission factors for natural gas combined cycle power plants? Please provide the range and average."
    wind_query = "What are the lifecycle greenhouse gas emissions of wind power technology? Please provide the emission range"
    
    print("\nExecuting all queries in parallel...")
    responses = await asyncio.gather(
        run_single_query(qa_chain, coal_query),
        run_single_query(qa_chain, gas_query),
        run_single_query(qa_chain, wind_query)
    )
    
    coal_response, gas_response, wind_response = responses
    print("All queries completed.")
    
    print("\n--- LLM Original Response ---")
    print(f"Coal response: {coal_response}")
    print(f"Gas response: {gas_response}")
    print(f"Wind response: {wind_response}")
    print("----------------------\n")
    
    # Use the more robust extract_emission_factor function for all technologies
    print("\n=== EXTRACTING COAL DATA ===")
    coal_data = extract_emission_factor(coal_response, 'coal')
    print(f"Coal result: {coal_data}")
    
    print("\n=== EXTRACTING GAS DATA ===")
    gas_data = extract_emission_factor(gas_response, 'gas')
    print(f"Gas result: {gas_data}")
    
    print("\n=== EXTRACTING WIND DATA ===")
    wind_data = extract_emission_factor(wind_response, 'wind')
    print(f"Wind result: {wind_data}")
    
    formatted_results = [
        format_emission_factor_result("Coal", coal_data),
        format_emission_factor_result("Gas", gas_data),
        format_emission_factor_result("Green", wind_data)
    ]
    
    return formatted_results

async def main():
    try:
        results = await get_power_range_from_rag()
        
        print("\n=== Comprehensive Emission Factor Results ===")
        for result in results:
            print(f"  {result}")
            
    except Exception as e:
        print(f"Serious error occurred during execution: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 