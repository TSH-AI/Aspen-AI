import win32com.client
import os
from datetime import datetime
import glob
import shutil

# ====================== File path and name configuration ======================
# Basic directory configuration
BASE_DIR = "inp_generate/simple"
LEARNING_FILES_DIR = "inp_outputs"
GUIDE_FILES_DIR = "input_guide"

# New: Filtered files storage directory configuration
SELECTED_FILES_ROOT = "selected_files"
DSTWU_SELECTED_DIR = os.path.join(SELECTED_FILES_ROOT, "dstwu_models")
RADFRAC_SELECTED_DIR = os.path.join(SELECTED_FILES_ROOT, "radfrac_models")
RADFRAC_KEYWORD_DIR = os.path.join(SELECTED_FILES_ROOT, "radfrac_keyword_models")
SENSITIVITY_KEYWORD_DIR = os.path.join(SELECTED_FILES_ROOT, "sensitivity_keyword_models")
DESIGN_SPEC_KEYWORD_DIR = os.path.join(SELECTED_FILES_ROOT, "design_spec_keyword_models")
EXCLUDED_FILES_DIR = os.path.join(SELECTED_FILES_ROOT, "excluded_large_files")

# automatically generate filename prefixes using the current date
current_date = datetime.now().strftime("%b %d").lower()  # in the format like "mar 29"
FILE_PREFIX = current_date

# output file configuration (all files use UTF-8 encoding)
DSTWU_FILES = {
    "input": os.path.join(BASE_DIR, f"{FILE_PREFIX}dstsimple-general.inp"),
    "report": os.path.join(BASE_DIR, f"{FILE_PREFIX}dstsimple-general.rep")
}

RADFRAC_FILES = {
    "input": os.path.join(BASE_DIR, f"{FILE_PREFIX}radsimple-general.inp"),
    "report": os.path.join(BASE_DIR, f"{FILE_PREFIX}radsimple-general.rep")
}

# Define file paths as constants for easy access
DSTWU_INPUT_FILE = DSTWU_FILES["input"]
DSTWU_REPORT_FILE = DSTWU_FILES["report"]
RADFRAC_INPUT_FILE = RADFRAC_FILES["input"]
RADFRAC_REPORT_FILE = RADFRAC_FILES["report"]

# File path getter functions for easy access
def get_dstwu_input_file():
    """Get the DSTWU input file path"""
    return DSTWU_INPUT_FILE

def get_dstwu_report_file():
    """Get the DSTWU report file path"""
    return DSTWU_REPORT_FILE

def get_radfrac_input_file():
    """Get the RadFrac input file path"""
    return RADFRAC_INPUT_FILE

def get_radfrac_report_file():
    """Get the RadFrac report file path"""
    return RADFRAC_REPORT_FILE

def get_all_generated_files():
    """Get all generated file paths as a dictionary"""
    return {
        "dstwu_input": DSTWU_INPUT_FILE,
        "dstwu_report": DSTWU_REPORT_FILE,
        "radfrac_input": RADFRAC_INPUT_FILE,
        "radfrac_report": RADFRAC_REPORT_FILE
    }


# ====================== Helper Functions ======================
def clear_directory_contents(directory_path):
    """Clear all contents of a directory safely"""
    if not os.path.exists(directory_path):
        return True
    
    deleted_count = 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_count += 1
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                deleted_count += 1
        except Exception as e:
            print(f"⚠️  Warning: Could not delete {filename}: {e}")
    
    if deleted_count > 0:
        print(f"🗑️  Cleared {deleted_count} items from {os.path.basename(directory_path)}")
    
    return True

def create_selected_file_directories(clear_previous=True):
    """Create filtered files storage directories and optionally clear previous contents"""
    directories = [
        SELECTED_FILES_ROOT, 
        DSTWU_SELECTED_DIR, 
        RADFRAC_SELECTED_DIR, 
        RADFRAC_KEYWORD_DIR,
        SENSITIVITY_KEYWORD_DIR,
        DESIGN_SPEC_KEYWORD_DIR,
        EXCLUDED_FILES_DIR
    ]
    
    if clear_previous:
        print("\n🧹 Clearing previous classification results...")
    else:
        print("\n📁 Preparing directories for classification...")
    
    for directory in directories:
        try:
            # Create directory if it doesn't exist
            os.makedirs(directory, exist_ok=True)
            
            # Clear all contents in the directory if requested
            if clear_previous:
                clear_directory_contents(directory)
            
            print(f"✓ Directory ready: {directory}")
        except Exception as e:
            print(f"× Failed to prepare directory {directory}: {e}")
    
    if clear_previous:
        print("✅ All directories cleared and ready for new classification\n")
    else:
        print("✅ All directories ready for classification\n")
    
    return True


def copy_file_to_category(source_path, target_dir, category_name):
    """Copy file to specified category directory"""
    try:
        filename = os.path.basename(source_path)
        target_path = os.path.join(target_dir, filename)
        
        # If target file exists, add timestamp to avoid overwriting
        if os.path.exists(target_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%H%M%S")
            filename = f"{name}_{timestamp}{ext}"
            target_path = os.path.join(target_dir, filename)
        
        shutil.copy2(source_path, target_path)
        print(f"  📄 Copied to {category_name}: {filename}")
        return True
    except Exception as e:
        print(f"  × Failed to copy file {os.path.basename(source_path)}: {e}")
        return False


def is_dstwu_related(content):
    """Check if content is related to DSTWU shortcut model and methanol-ethanol distillation"""
    content_upper = content.upper()
    return (
        "DSTWU" in content_upper or  # Include if DSTWU is present
        ("CH4O" in content_upper and "C2H6O-2" in content_upper)  # OR include if both chemicals are present
    )


def is_radfrac_related(content):
    """Check if content is related to RadFrac rigorous model with design specs/sensitivity"""
    content_upper = content.upper()
    # Initialize counters if they don't exist
    if not hasattr(is_radfrac_related, 'radfrac_count'):
        is_radfrac_related.radfrac_count = 0
    if not hasattr(is_radfrac_related, 'design_spec_count'):
        is_radfrac_related.design_spec_count = 0
    if not hasattr(is_radfrac_related, 'sensitivity_count'):
        is_radfrac_related.sensitivity_count = 0
    
    # Check if we've reached the limit for either keyword
    if is_radfrac_related.radfrac_count >= 8 and is_radfrac_related.sensitivity_count >= 8:
        return False
    
    # Check content and update counters
    has_radfrac = "RADFRAC" in content_upper and "DP-COL" in content_upper and is_radfrac_related.radfrac_count <10
    has_sensitivity = "SENSITIVITY" in content_upper and is_radfrac_related.sensitivity_count < 7
    has_design_spec = "DESIGN-SPEC" in content_upper and is_radfrac_related.design_spec_count < 7

    if has_radfrac:
        is_radfrac_related.radfrac_count += 1
    if has_sensitivity:
        is_radfrac_related.sensitivity_count += 1
    if has_design_spec:
        is_radfrac_related.design_spec_count += 1
    
    return has_radfrac or has_sensitivity or has_design_spec


def read_and_classify_files(file_list):
    """Read and classify files, return file name list and copy files to organized folders"""
    dstwu_files = []  # Store shortcut model file information (including file name)
    radfrac_files = []  # Store rigorous model file information
    radfrac_keyword_files = []  # Store files with RADFRAC keyword
    sensitivity_keyword_files = []  # Store files with SENSITIVITY keyword
    design_spec_keyword_files = []  # Store files with DESIGN-SPEC keyword
    excluded_large_files = []  # Store RADFRAC files excluded due to size

    # Counters for file copying
    dstwu_copied = 0
    radfrac_copied = 0
    radfrac_keyword_copied = 0
    sensitivity_keyword_copied = 0
    design_spec_keyword_copied = 0
    excluded_copied = 0

    for file_info in file_list:
        content = None
        # Try different encodings to read the file
        encodings = [file_info["encoding"], "gb18030", "ansi", "utf-16"]
        for encoding in encodings:
            try:
                with open(file_info["path"], "r", encoding=encoding) as f:
                    content = f.read()
                break
            except:
                continue

        if not content:
            print(f"× Cannot read file (skipped): {file_info['path']}")
            continue

        filename = os.path.basename(file_info["path"])
        file_data = {
            "path": file_info["path"],
            "name": filename,
            "content": content,
            "size": len(content)
        }

        # Classification logic with file copying
        if is_dstwu_related(content):
            dstwu_files.append(file_data)
            print(f"✓ Shortcut Model: {filename}")
            if copy_file_to_category(file_info["path"], DSTWU_SELECTED_DIR, "DSTWU Models"):
                dstwu_copied += 1
        elif is_radfrac_related(content):
            # Check file size, exclude files larger than 20KB
            file_size_kb = file_data["size"] / 1024
            if file_data["size"] <= 20480:  # 20KB = 20480 characters
                radfrac_files.append(file_data)
                print(f"✓ Rigorous Model: {filename} ({file_size_kb:.2f} KB)")
                if copy_file_to_category(file_info["path"], RADFRAC_SELECTED_DIR, "RadFrac Models"):
                    radfrac_copied += 1
                
                # Additional classification by keywords
                content_upper = content.upper()
                if "RADFRAC" in content_upper and "DP-COL" in content_upper:
                    radfrac_keyword_files.append(file_data)
                    if copy_file_to_category(file_info["path"], RADFRAC_KEYWORD_DIR, "RadFrac Keyword Models"):
                        radfrac_keyword_copied += 1
                
                if "SENSITIVITY" in content_upper:
                    sensitivity_keyword_files.append(file_data)
                    if copy_file_to_category(file_info["path"], SENSITIVITY_KEYWORD_DIR, "Sensitivity Keyword Models"):
                        sensitivity_keyword_copied += 1
                
                if "DESIGN-SPEC" in content_upper:
                    design_spec_keyword_files.append(file_data)
                    if copy_file_to_category(file_info["path"], DESIGN_SPEC_KEYWORD_DIR, "Design-Spec Keyword Models"):
                        design_spec_keyword_copied += 1
            else:
                print(f"× Rigorous model file too large (skipped): {filename} ({file_size_kb:.2f} KB > 20 KB)")
                excluded_large_files.append(file_data)
                if copy_file_to_category(file_info["path"], EXCLUDED_FILES_DIR, "Large Files"):
                    excluded_copied += 1
        else:
            print(f"× Unclassified file: {filename}")

    # Print classification statistics
    print("\n" + "=" * 50)
    print("📊 File Classification and Copy Results:")
    print(f"Shortcut Model Files (DSTWU): {len(dstwu_files)} (Copied: {dstwu_copied})")
    print(f"Rigorous Model Files (RadFrac): {len(radfrac_files)} (Copied: {radfrac_copied})")
    print(f"RadFrac Keyword Files: {len(radfrac_keyword_files)} (Copied: {radfrac_keyword_copied})")
    print(f"Sensitivity Keyword Files: {len(sensitivity_keyword_files)} (Copied: {sensitivity_keyword_copied})")
    print(f"Design-Spec Keyword Files: {len(design_spec_keyword_files)} (Copied: {design_spec_keyword_copied})")
    if excluded_large_files:
        excluded_total_size = sum(f["size"] for f in excluded_large_files)
        print(f"Excluded Large Files (>20KB): {len(excluded_large_files)} (Copied: {excluded_copied}), Total Size {excluded_total_size/1024:.2f} KB")
    
    # Calculate file size statistics
    dstwu_total_size = sum(f["size"] for f in dstwu_files)
    radfrac_total_size = sum(f["size"] for f in radfrac_files)
    radfrac_keyword_total_size = sum(f["size"] for f in radfrac_keyword_files)
    sensitivity_keyword_total_size = sum(f["size"] for f in sensitivity_keyword_files)
    design_spec_keyword_total_size = sum(f["size"] for f in design_spec_keyword_files)
    total_size = dstwu_total_size + radfrac_total_size
    
    print("\n📈 File Size Statistics:")
    print(f"Shortcut Model Files (DSTWU) Total Size: {dstwu_total_size:,} characters ({dstwu_total_size/1024:.2f} KB)")
    print(f"Rigorous Model Files (RadFrac) Total Size: {radfrac_total_size:,} characters ({radfrac_total_size/1024:.2f} KB)")
    print(f"RadFrac Keyword Files Total Size: {radfrac_keyword_total_size:,} characters ({radfrac_keyword_total_size/1024:.2f} KB)")
    print(f"Sensitivity Keyword Files Total Size: {sensitivity_keyword_total_size:,} characters ({sensitivity_keyword_total_size/1024:.2f} KB)")
    print(f"Design-Spec Keyword Files Total Size: {design_spec_keyword_total_size:,} characters ({design_spec_keyword_total_size/1024:.2f} KB)")
    print(f"Selected Files Total Size: {total_size:,} characters ({total_size/1024:.2f} KB)")
    
    print("\n📁 Files Organization:")
    print(f"DSTWU model files stored in: {DSTWU_SELECTED_DIR}")
    print(f"RadFrac model files stored in: {RADFRAC_SELECTED_DIR}")
    print(f"RadFrac keyword files stored in: {RADFRAC_KEYWORD_DIR}")
    print(f"Sensitivity keyword files stored in: {SENSITIVITY_KEYWORD_DIR}")
    print(f"Design-Spec keyword files stored in: {DESIGN_SPEC_KEYWORD_DIR}")
    print(f"Large files stored in: {EXCLUDED_FILES_DIR}")
    print("=" * 50 + "\n")

    # Return sorted contents and file name list
    return (
        {
            "contents": [x["content"] for x in sorted(dstwu_files, key=lambda x: -x["size"])],
            "file_names": [x["name"] for x in dstwu_files],
            "total_size": dstwu_total_size,
            "file_count": len(dstwu_files)
        },
        {
            "contents": [x["content"] for x in sorted(radfrac_files, key=lambda x: -x["size"])],
            "file_names": [x["name"] for x in radfrac_files],
            "total_size": radfrac_total_size,
            "file_count": len(radfrac_files)
        },
        excluded_large_files
    )


def run_aspen_simulation(input_file, report_name):
    """Run Aspen Plus simulation and export report"""
    aspen_instance = None
    try:
        print(f"\nRunning Aspen simulation: {os.path.basename(input_file)}")
        aspen_instance = win32com.client.Dispatch("Apwn.Document")
        print("Aspen Plus object created.")

        abs_input_file = os.path.abspath(input_file)
        abs_report_name = os.path.abspath(report_name)
        print(f"Absolute input path: {abs_input_file}")

        aspen_instance.InitFromArchive2(abs_input_file)
        print("Initialized from archive.")

        aspen_instance.Visible = True
        aspen_instance.SuppressDialogs = 1

        aspen_instance.Reinit()
        print("Reinitialized.")
        aspen_instance.Engine.Run2()
        print("Simulation completed.")

        aspen_instance.Export(2, abs_report_name)
        print(f"Report exported to {abs_report_name}")

        return True
    except Exception as e:
        print(f"Aspen simulation error: {e}")
        return False
    finally:
        if aspen_instance:
            try:
                aspen_instance.Close()
                print("Aspen instance closed.")
            except Exception as close_e:
                print(f"Warning: Error closing Aspen: {close_e}")
        aspen_instance = None
        import gc
        gc.collect()


def analyze_radfrac_files(file_list):
    """Analyze keyword statistics for RadFrac related files"""
    radfrac_count = 0
    sensitivity_count = 0
    design_spec_count = 0
    total_size = 0
    
    for file_info in file_list:
        content = None
        # Try different encodings to read the file
        encodings = [file_info["encoding"], "gb18030", "ansi", "utf-16"]
        for encoding in encodings:
            try:
                with open(file_info["path"], "r", encoding=encoding) as f:
                    content = f.read()
                break
            except:
                continue

        if not content:
            continue

        content_upper = content.upper()
        if "RADFRAC" in content_upper:
            radfrac_count += 1
        if "SENSITIVITY" in content_upper:
            sensitivity_count += 1
        if "DESIGN-SPEC" in content_upper:
            design_spec_count += 1
        
        total_size += len(content)

    return {
        "radfrac_count": radfrac_count,
        "sensitivity_count": sensitivity_count,
        "design_spec_count": design_spec_count,
        "total_size": total_size
    }


def read_guide_files():
    """Read Aspen input guide files"""
    guide_files = [
        "15 Rigorous Distillation_RADFRAC.md",
        "30 Design Specifications.md", 
        "35 Sensitivity Blocks.md"
    ]
    
    guide_contents = ""
    
    for filename in guide_files:
        filepath = os.path.join(GUIDE_FILES_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                guide_contents += f"\n\n=== {filename} ===\n{content}\n"
                print(f"✓ Guide file read: {filename}")
        except Exception as e:
            print(f"× Cannot read guide file {filename}: {e}")
            continue
    
    return guide_contents


# ====================== Main Execution ======================
os.environ["SERPER_API_KEY"] = "<your api key>"

from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Initialize LLM
# model = ChatOpenAI(model="<your model>", api_key="<your api key>",
#                    base_url="<your base url>", temperature=0)

model = ChatOpenAI(model="<your model>", api_key="<your api key>",
                   base_url="<your base url>", temperature=0)

# Get all learning files
LEARNING_FILES = []
for filepath in glob.glob(os.path.join(LEARNING_FILES_DIR, "*.inp")):
    LEARNING_FILES.append({"path": filepath, "encoding": "utf-8"})
print(f"Found {len(LEARNING_FILES)} .inp files in {LEARNING_FILES_DIR}")

# Create selected file directories
create_selected_file_directories()

# Read and classify files
print("\n--- Reading and Classifying Files ---")
dstwu_data, radfrac_data, excluded_large_files = read_and_classify_files(LEARNING_FILES)

# Analyze RadFrac files
radfrac_stats = analyze_radfrac_files(LEARNING_FILES)
print("\nRadFrac File Analysis Results:")
print("-"*40)
print(f"Files containing RADFRAC keyword: {radfrac_stats['radfrac_count']}")
print(f"Files containing SENSITIVITY keyword: {radfrac_stats['sensitivity_count']}")
print(f"Files containing DESIGN-SPEC keyword: {radfrac_stats['design_spec_count']}")
print(f"Total size of all RadFrac related files: {radfrac_stats['total_size']/1024:.2f} KB")
print("-"*40)

# Print final selection results
print("\nFinal Selected Files List:")
print("-"*40)
print(f"Shortcut Model Files (DSTWU): {dstwu_data['file_count']} files, Total Size {dstwu_data['total_size']:,} characters ({dstwu_data['total_size']/1024:.2f} KB)")
for i, name in enumerate(dstwu_data["file_names"], 1):
    print(f"{i}. {name}")

print(f"\nRigorous Model Files (RadFrac): {radfrac_data['file_count']} files, Total Size {radfrac_data['total_size']:,} characters ({radfrac_data['total_size']/1024:.2f} KB)")
for i, name in enumerate(radfrac_data["file_names"], 1):
    print(f"{i}. {name}")

print("-"*40)
print(f"Total Selected Files: {dstwu_data['file_count'] + radfrac_data['file_count']}")
print(f"Total File Size: {dstwu_data['total_size'] + radfrac_data['total_size']:,} characters ({(dstwu_data['total_size'] + radfrac_data['total_size'])/1024:.2f} KB)")

# Display excluded large files information
if excluded_large_files:
    excluded_total_size = sum(f["size"] for f in excluded_large_files)
    print(f"\nRadFrac files excluded due to size (>20KB): {len(excluded_large_files)} files, Total Size {excluded_total_size/1024:.2f} KB")
    for i, file_data in enumerate(excluded_large_files, 1):
        print(f"  {i}. {file_data['name']} ({file_data['size']/1024:.2f} KB)")

print("-"*40)

# Get actual contents
dstwu_learning_contents = dstwu_data["contents"]
radfrac_learning_contents = radfrac_data["contents"]

# Read Aspen input guide files
print("\n--- Reading Aspen Input Guide Files ---")
guide_contents = read_guide_files()

# Initialize conversation chain
memory = ConversationBufferMemory(return_messages=True)
chain = ConversationChain(llm=model, memory=memory)

# ====================== DSTWU Shortcut Model ======================
print("\n--- Generating DSTWU model ---")

# Step 1: Calculate recovery rates
print("\nStep 1: Calculating recovery rates...")
prompt_recovery = """You are a chemical engineer with exceptional mathematical calculation skills. Calculate the following values and show your detailed work.

GIVEN VALUES:
F = 100 kg/h (Feed flow rate)
xF = 0.40 (Feed methanol mass fraction)
xD = 0.98 (Distillate methanol mass fraction)
xB = 0.02 (Bottoms methanol mass fraction)

REQUIRED CALCULATIONS:
1. Calculate D (distillate flow rate):
   D = F * (xF - xB) / (xD - xB)
   Show all steps and unit checks

2. Calculate B (bottoms flow rate):
   B = F - D
   Verify mass balance

3. Calculate RECOVL (methanol recovery):
   RECOVL = (D * xD) / (F * xF)
   Show fraction simplification

4. Calculate RECOVH (ethanol recovery):
   RECOVH = (D * (1 - xD)) / (F * (1 - xF))
   Show fraction simplification

IMPORTANT: After showing all calculations, end your response with exactly these characters:
FINAL_RESULTS_BEGIN
[your first number]
[your second number]
[your third number]
[your fourth number]
FINAL_RESULTS_END

The numbers between these markers must be in this order:
1. RECOVL (as decimal)
2. RECOVH (as decimal)
3. D (in kg/h)
4. B (in kg/h)"""

try:
    answer_recovery = chain.invoke({"input": prompt_recovery})
    response_text = answer_recovery['response']
    
    # Extract the values between the markers
    start_marker = "FINAL_RESULTS_BEGIN"
    end_marker = "FINAL_RESULTS_END"
    
    start_idx = response_text.find(start_marker)
    end_idx = response_text.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find result markers in response")
        
    # Extract and split the results section
    results_section = response_text[start_idx + len(start_marker):end_idx].strip()
    recovery_values = results_section.split('\n')
    
    # Print the calculation process
    print("\nDetailed Calculation Process:")
    print(response_text[:start_idx].strip())
    
    # Parse the final values
    RECOVL = float(recovery_values[0])
    RECOVH = float(recovery_values[1])
    D = float(recovery_values[2])
    B = float(recovery_values[3])
    
    print(f"Calculated recovery rates:")
    print(f"RECOVL (Methanol): {RECOVL:.4f}")
    print(f"RECOVH (Ethanol): {RECOVH:.4f}")
    print(f"Distillate rate (D): {D:.2f} kg/h")
    print(f"Bottom rate (B): {B:.2f} kg/h")

    # Step 2: Generate DSTWU input file
    print("\nStep 2: Generating DSTWU input file...")
    prompt_dstwu = f"""
Generate a shortcut distillation model (DSTWU) input file for methanol-ethanol separation.

1. Process Parameters
- RECOVL (Methanol recovery): {RECOVL:.4f}
- RECOVH (Ethanol recovery): {RECOVH:.4f}

2. Key Requirements
2.1 Feed Conditions:
   - Flow rate: 100 kg/h
   - Temperature: 20°C
   - Pressure: 1.3 atm
   - Composition: 40 wt% methanol, 60 wt% ethanol

2.2 Distillation Targets:
   - Top stream: 98 wt% methanol
   - Bottom stream: 2 wt% methanol
   - Top pressure: 1 atm
   - Bottom pressure: estimated from the top pressure and the pressure drop of the column
   - Reflux ratio (RR): -1.2

2.3 Input File Structure:
   - **Carefully write the name of every unit and ensure IN-UNITS section is complete**
   - **Ensure the name of every unit comply with the example files**
   - **Use "&" for line breaks if needed**
   - **Only use MASS-FLOW for methanol and ethanol in feed stream**
   - **Don't use MASS-FRAC for feed stream**
   - **Use SI units for all variables and pressure in atm**
   - The first two lines of the file describes the Aspen Plus version, creation time and file directory path 
   - Carefully learn the content of the very beginning linesfrom the example files 
   - Include physical property database parameters
   - Note that if a line is too long, you can add "&" to break the line. This is what the input files do. 
   - Don't forget the semicolon at the beginning and end of the file

3. Output Format
   - **No annotation text**
   - **No intermediate calculations**
   - **Use SI units not MET units and pressure in atm**
   - Follow example file format
""" + "".join(dstwu_learning_contents)

    print("Generating DSTWU model...")
    answer_dst = chain.invoke({"input": prompt_dstwu})
    input_content_dst = answer_dst['response']

    if input_content_dst:
        with open(DSTWU_INPUT_FILE, "w", encoding="utf-8") as f:
            f.write(input_content_dst)
        print(f"DSTWU input saved to {DSTWU_INPUT_FILE}")

        # Run simulation
        if run_aspen_simulation(DSTWU_INPUT_FILE, DSTWU_REPORT_FILE):
            try:
                with open(DSTWU_REPORT_FILE, "r", encoding="utf-8") as f:
                    rep_content_dst = f.read()
                print("DSTWU simulation completed successfully.")
            except Exception as e:
                print(f"Error reading DSTWU report: {e}")
                rep_content_dst = ""
        else:
            rep_content_dst = ""
            print("DSTWU simulation failed.")
    else:
        rep_content_dst = ""
        print("DSTWU generation failed.")
except Exception as e:
    print(f"Error in DSTWU generation: {e}")
    rep_content_dst = ""

# ====================== RADFRAC Rigorous Model ======================
if rep_content_dst:
    print("\n--- Generating RadFrac model ---")

    prompt = """    
Utilize maximum model capacity to execute the following tasks based on provided input files.
The part pinched by ** is crucial and must be strictly followed.
Each module must adhere to its own requirements without cross-mixing

Generate a Rigorous distillation model (RADFRAC) input file with design specification and sensitivity analysis for methanol-ethanol separation using the input file guide and examples.
In the part of Rigorous Distillation System Design, use the shortcut model report to set the parameters needed in the Radfrac input file. 
Remember to add the design specification to the Radfrac input file. Set the design specification that change the molar reflux ratio to reach a targeted distillate composition of 98wt% methanol.
Design the sensitivity analysis that study the variation trends of reflux ratio and rebolier duties under different stages, and feed stage location.  The kind of variables and the "SENTENCE"should be written carefully

1. Aspen Input File Guide References
**Refer to the following official Aspen input guide files for additional guidance on proper formatting and syntax:**
""" + guide_contents + """

**End of Guide References - Use these to ensure proper Aspen Plus input file syntax and structure.**

2. Input File Processing
2.1 Primary File: The first file contains the shortcut model report. Extract all valid data from this report.
**=== SHORTCUT MODEL REPORT ===**
""" + rep_content_dst + """
**=== END OF SHORTCUT MODEL REPORT ===**

2.2 Supplementary Files: Use the remaining files to learn how to write a model for radfrac. Strictly follow the format of the examples, including spacing.
**=== RADFRAC EXAMPLE FILES ===**
""" + "".join(radfrac_learning_contents) + """
**=== END OF RADFRAC EXAMPLE FILES ===**

3. Key Requirements
3.1 Basic Setup:
   - **Strictly adhere to the input file guide format for the radfrac part, especially the format of pressure setting for column**
   - Use same feed conditions as shortcut model, but set the stage number and feed stage position (rounded to multiple of 10) as 10 times of the shortcut model
   - Don't forget to set the distillate rate or the D/F ratio and pay attention to the mass flow or the mole flow
   - Set pressure based on shortcut model and set the pressure drop of the column reasonably in the Radfrac part
   - Don't forget to set the pressure drop of the column (DP-COL) in the Radfrac part
   - Set the reflux ratio as 1 to achieve convergence easily
   - The maximum iterations number should be set as 200 to get the most accurate results

3.2 Design Specification:
   - **Remember to set the upper and lower limit of reflux ratio in the design specification according to the input file guide**
   - Control distillate composition (98wt% methanol)
   - Use reflux ratio as manipulated variable
   - Set the tolerance of the design specification as 0.0001

4. Sensitivity Analysis:
   - sensitivity analysis 1: find the minimum reflux ratio
     * explore the variation trends of reflux ratio under different numbers of stages and feed stage position in the sensitivity part.
     * The range of the number of stages should be set widely 
       - the maximum number of stages should be set the same as the number of stages of the radfrac model
       - the minimum number of stages should be set a little smaller than 100
       - the incremental should be set as 20 to get appropriate data points.
     * The feed stage position should be set reasonably according to the range of the number of stages 
       - the maximum feed stage should be set 10 larger than half of the maximum number of stages set above
       - the minimum feed stage should be set 10 smaller than half of the minimum number of stages set above
       - the incremental can be set as 10.
   - sensitivity analysis 2: Explore the variation trends of reflux ratio, and reboiler heat duty under different numbers of stages and feed stage position in the range of the shortcut model
     * The range of the number of stages should be set according to the number of stages of the DSTWU model
       - the maximum number of stages should be set a little larger than the number of stages of the DSTWU model but smaller than 50
       - the minimum number of stages should be set reasonably to get 20-30 data points
       - the incremental should be set as 1.
     * The feed stage position should be set reasonably according to the range of the number of stages
       - the maximum feed stage should be set 10 larger than half of the maximum number of stages set above
       - the minimum feed stage should be set no more than half of the minimum number of stages set above
       - the incremental can be set as 1.     
   - Use "RESULTS" for the sentence of all variables and don't add the "UOM" section
   - The format of the sensitivity analysis should strictly comply with the input file guide
   - Remember to reinitialize all blocks in the sensitivity analysis
   - **The type of reflux ratio is calculated reflux ratio (RR) rather than the specified reflux ratio.**
   - **Don't forget the OPT-LIST section in the RANGE part of the sensitivity analysis**

5. Output Format
   - **No annotation text**
   - Use "&" for line breaks
   - Use SI units
   - All variable names in the DESIGN-SPEC section and the SENSITIVITY section should only contain capital letters and numbers but not over 8 characters
   - Pay attention to the beginning/ending semicolons
"""

    try:
        answer_rad = chain.invoke({"input": prompt})
        input_content_rad = answer_rad['response']

        if input_content_rad:
            with open(RADFRAC_INPUT_FILE, "w", encoding="utf-8") as f:
                f.write(input_content_rad)
            print(f"RadFrac input saved to {RADFRAC_INPUT_FILE}")

            # Run simulation
            if run_aspen_simulation(RADFRAC_INPUT_FILE, RADFRAC_REPORT_FILE):
                print("RadFrac simulation completed.")
            else:
                print("RadFrac simulation failed.")
        else:
            print("RadFrac generation failed.")
    except Exception as e:
        print(f"Error in RadFrac generation: {e}")
else:
    print("\nSkipping RadFrac generation due to missing DSTWU report.")

# ====================== Generate File Classification Summary ======================
def generate_classification_summary():
    """Generate file classification summary report"""
    # Add timestamp to avoid overwriting previous reports
    timestamp = datetime.now().strftime("%H%M%S")
    summary_file = os.path.join(SELECTED_FILES_ROOT, f"{FILE_PREFIX}_classification_summary_{timestamp}.txt")
    
    try:
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write("File Classification Summary Report\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("📁 Directory Structure:\n")
            f.write(f"Main Directory: {SELECTED_FILES_ROOT}\n")
            f.write(f"├── dstwu_models/          (DSTWU shortcut model files)\n")
            f.write(f"├── radfrac_models/        (RadFrac rigorous model files)\n")
            f.write(f"├── radfrac_keyword_models/    (Files with RADFRAC keyword)\n")
            f.write(f"├── sensitivity_keyword_models/ (Files with SENSITIVITY keyword)\n")
            f.write(f"├── design_spec_keyword_models/ (Files with DESIGN-SPEC keyword)\n")
            f.write(f"└── excluded_large_files/  (Large files, >20KB)\n\n")
            
            # Count files in each directory
            for dir_name, dir_path, description in [
                ("DSTWU Models", DSTWU_SELECTED_DIR, "Shortcut model related files"),
                ("RadFrac Models", RADFRAC_SELECTED_DIR, "Rigorous model related files"),
                ("RadFrac Keyword Models", RADFRAC_KEYWORD_DIR, "Files with RADFRAC keyword"),
                ("Sensitivity Keyword Models", SENSITIVITY_KEYWORD_DIR, "Files with SENSITIVITY keyword"),
                ("Design-Spec Keyword Models", DESIGN_SPEC_KEYWORD_DIR, "Files with DESIGN-SPEC keyword"),
                ("Large Files", EXCLUDED_FILES_DIR, "Excluded large files")
            ]:
                f.write(f"📂 {dir_name} ({description}):\n")
                f.write(f"Directory Path: {dir_path}\n")
                
                if os.path.exists(dir_path):
                    files = [f for f in os.listdir(dir_path) if f.endswith('.inp')]
                    f.write(f"File Count: {len(files)}\n")
                    
                    if files:
                        f.write("File List:\n")
                        for i, filename in enumerate(sorted(files), 1):
                            f.write(f"  {i:2d}. {filename}\n")
                    else:
                        f.write("  (No files)\n")
                else:
                    f.write("Directory does not exist\n")
                f.write("\n")
            
            f.write("=" * 60 + "\n")
            f.write("Description:\n")
            f.write("• DSTWU Models: Shortcut distillation models for quick estimation\n")
            f.write("• RadFrac Models: Rigorous tray models with design specifications and sensitivity analysis\n")
            f.write("• RadFrac Keyword Models: Files containing RADFRAC keyword and DP-COL\n")
            f.write("• Sensitivity Keyword Models: Files containing SENSITIVITY keyword\n")
            f.write("• Design-Spec Keyword Models: Files containing DESIGN-SPEC keyword\n")
            f.write("• Large Files: RadFrac files larger than 20KB, excluded due to size\n")
            f.write("• All files are automatically filtered and classified from original learning files\n")
        
        print(f"✓ File classification summary report generated: {summary_file}")
        return True
    except Exception as e:
        print(f"× Failed to generate summary report: {e}")
        return False

# Generate classification summary report
generate_classification_summary()

print("\n" + "=" * 60)
print("🎉 Script execution completed!")
print("📁 Filtered files have been organized by category in:")
print(f"   {SELECTED_FILES_ROOT}")
print("📋 Please check the summary report for detailed classification information")

# Display generated file paths for easy access
print("\n📄 Generated File Paths:")
print(f"DSTWU Input: {DSTWU_INPUT_FILE}")
print(f"DSTWU Report: {DSTWU_REPORT_FILE}")
print(f"RadFrac Input: {RADFRAC_INPUT_FILE}")
print(f"RadFrac Report: {RADFRAC_REPORT_FILE}")

print("\n💡 Usage Examples:")
print("# Access individual files:")
print(f"# dstwu_input = get_dstwu_input_file()")
print(f"# radfrac_report = get_radfrac_report_file()")
print("# Get all files:")
print(f"# all_files = get_all_generated_files()")

print("=" * 60)

