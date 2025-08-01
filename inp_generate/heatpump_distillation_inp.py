import win32com.client
import os
from datetime import datetime
import glob
import shutil
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ====================== File path and name configuration ======================
# Basic directory configuration
BASE_DIR = "inp_generate/difficult"
LEARNING_FILES_DIR = "inp_outputs"
GUIDE_FILES_DIR = "input_guide_difficult"

# Existing process file path - dynamically generated based on current date
current_date = datetime.now().strftime("%b %d").lower()  # in the format like "mar 29"
EXISTING_PROCESS_FILE = os.path.join("inp_generate/simple", f"{current_date}radsimpleo.inp")
EXISTING_PROCESS_REPORT = os.path.join("inp_generate/simple", f"{current_date}radsimpleo.rep")

# Filtered files output directory
FILTERED_FILES_DIR = os.path.join(BASE_DIR, f"filtered_heat_pump_files_{current_date}")

# automatically generate filename prefixes using the current date
FILE_PREFIX = current_date

model = ChatOpenAI(model="<your model>", api_key="<your api key>",
                   base_url="<your base url>", temperature=0)

# Get model name from the model configuration and replace special characters
MODEL_NAME = model.model_name.replace('/', '_').replace('-', '_')  # Replace special characters with underscores

# output file configuration (all files use UTF-8 encoding)
HEAT_PUMP_FILES = {
    "input": os.path.join(BASE_DIR, f"{FILE_PREFIX}heat_pump_design.inp"),
    "report": os.path.join(BASE_DIR, f"{FILE_PREFIX}heat_pump_design.rep")
}


# ====================== Helper Functions ======================
def read_and_classify_files(file_list):
    """Read and classify files, filter heat pump distillation related files"""
    heat_pump_files = []  # Store heat pump distillation related file information
    excluded_large_files = []  # Store files excluded due to large size
    
    # Statistics for each criteria
    criteria_stats = {
        "FSPLIT": {"files": [], "total_size": 0},
        "HEATER": {"files": [], "total_size": 0},
        "RADFRAC": {"files": [], "total_size": 0},
        "COMPR": {"files": [], "total_size": 0},
        "INFO HEAT": {"files": [], "total_size": 0},
        "DESIGN-SPEC": {"files": [], "total_size": 0}  # Add DESIGN-SPEC criteria
    }
    
    # Counters for limited criteria
    heater_count = 0
    radfrac_count = 0
    compr_count = 0
    design_spec_count = 0  # Add counter for DESIGN-SPEC
    MAX_HEATER_FILES = 5
    MAX_RADFRAC_FILES = 5
    MAX_COMPR_FILES = 5
    MAX_DESIGN_SPEC_FILES = 5  # Add limit for DESIGN-SPEC files

    for file_info in file_list:
        content = None
        # Try reading files with different encodings
        encodings = [file_info["encoding"], "gb18030", "ansi", "utf-16"]
        for encoding in encodings:
            try:
                with open(file_info["path"], "r", encoding=encoding) as f:
                    content = f.read()
                break
            except:
                continue

        if not content:
            print(f"× Unable to read file (skipped): {file_info['path']}")
            continue

        filename = os.path.basename(file_info["path"])
        file_data = {
            "path": file_info["path"],
            "name": filename,
            "content": content,
            "size": len(content)
        }

        # Check which criteria this file matches with limits
        content_upper = content.upper()
        matched_criteria = []
        
        if "FSPLIT" in content_upper:
            matched_criteria.append("FSPLIT")
        if "HEATER" in content_upper and heater_count < MAX_HEATER_FILES:
            matched_criteria.append("HEATER")
        if "RADFRAC" in content_upper and radfrac_count < MAX_RADFRAC_FILES:
            matched_criteria.append("RADFRAC")
        if "COMPR" in content_upper and compr_count < MAX_COMPR_FILES:
            matched_criteria.append("COMPR")
        if "INFO HEAT" in content_upper:
            matched_criteria.append("INFO HEAT")
        if "DESIGN-SPEC" in content_upper and design_spec_count < MAX_DESIGN_SPEC_FILES:
            matched_criteria.append("DESIGN-SPEC")
        
        if matched_criteria:
            # Check file size, exclude files larger than 30KB
            file_size_kb = file_data["size"] / 1024
            if file_data["size"] <= 30720:  # 30KB = 30720 characters
                file_data["matched_criteria"] = matched_criteria
                heat_pump_files.append(file_data)
                
                # Update criteria statistics and counters
                for criterion in matched_criteria:
                    criteria_stats[criterion]["files"].append(filename)
                    criteria_stats[criterion]["total_size"] += file_data["size"]
                    
                    # Update limited counters
                    if criterion == "HEATER":
                        heater_count += 1
                    elif criterion == "RADFRAC":
                        radfrac_count += 1
                    elif criterion == "COMPR":
                        compr_count += 1
                    elif criterion == "DESIGN-SPEC":
                        design_spec_count += 1
                
                criteria_str = ", ".join(matched_criteria)
                print(f"✓ Heat pump distillation related: {filename} ({file_size_kb:.2f} KB) - Matches: [{criteria_str}]")
            else:
                criteria_str = ", ".join(matched_criteria)
                print(f"× Heat pump file too large (skipped): {filename} ({file_size_kb:.2f} KB > 30 KB) - Would match: [{criteria_str}]")
                excluded_large_files.append(file_data)
        else:
            # Check if file would match but limits reached
            skipped_criteria = []
            if "HEATER" in content_upper and heater_count >= MAX_HEATER_FILES:
                skipped_criteria.append("HEATER(limit reached)")
            if "RADFRAC" in content_upper and radfrac_count >= MAX_RADFRAC_FILES:
                skipped_criteria.append("RADFRAC(limit reached)")
            if "COMPR" in content_upper and compr_count >= MAX_COMPR_FILES:
                skipped_criteria.append("COMPR(limit reached)")
            if "DESIGN-SPEC" in content_upper and design_spec_count >= MAX_DESIGN_SPEC_FILES:
                skipped_criteria.append("DESIGN-SPEC(limit reached)")
            
            if skipped_criteria:
                skipped_str = ", ".join(skipped_criteria)
                print(f"× File limit reached (skipped): {filename} - Would match: [{skipped_str}]")
            else:
                print(f"× Unclassified file: {filename}")

    # Print classification statistics
    print("\n" + "=" * 60)
    print("File classification results:")
    print(f"Heat pump distillation related files: {len(heat_pump_files)} files")
    if excluded_large_files:
        excluded_total_size = sum(f["size"] for f in excluded_large_files)
        print(f"Excluded large files (>30KB): {len(excluded_large_files)} files, total size {excluded_total_size/1024:.2f} KB")
    
    # Print detailed statistics for each criteria
    print("\nDetailed statistics by filtering criteria:")
    print("-" * 60)
    for criterion, stats in criteria_stats.items():
        if stats["files"]:
            limit_info = ""
            if criterion == "HEATER":
                limit_info = f" (Limited to {MAX_HEATER_FILES} files)"
            elif criterion == "RADFRAC":
                limit_info = f" (Limited to {MAX_RADFRAC_FILES} files)"
            elif criterion == "COMPR":
                limit_info = f" (Limited to {MAX_COMPR_FILES} files)"
            elif criterion == "DESIGN-SPEC":
                limit_info = f" (Limited to {MAX_DESIGN_SPEC_FILES} files)"
            
            print(f"{criterion}{limit_info}:")
            print(f"  Files: {len(stats['files'])} files")
            print(f"  Total size: {stats['total_size']:,} characters ({stats['total_size']/1024:.2f} KB)")
            print(f"  Files list: {', '.join(stats['files'])}")
        else:
            print(f"{criterion}: No files found")
        print()
    
    # Calculate file size statistics
    heat_pump_total_size = sum(f["size"] for f in heat_pump_files)
    
    print("Overall file size statistics:")
    print(f"Heat pump distillation files total size: {heat_pump_total_size:,} characters ({heat_pump_total_size/1024:.2f} KB)")
    print("=" * 60 + "\n")

    # Return sorted content and file name list, plus criteria statistics
    return (
        {
            "contents": [x["content"] for x in sorted(heat_pump_files, key=lambda x: -x["size"])],
            "file_names": [x["name"] for x in heat_pump_files],
            "file_details": sorted(heat_pump_files, key=lambda x: -x["size"]),
            "total_size": heat_pump_total_size,
            "file_count": len(heat_pump_files),
            "criteria_stats": criteria_stats
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


def analyze_heat_pump_files(file_list):
    """Analyze heat pump distillation related files keyword statistics"""
    fsplit_count = 0
    heater_count = 0
    radfrac_count = 0
    compr_count = 0
    info_heat_count = 0
    total_size = 0
    
    for file_info in file_list:
        content = None
        # Try reading files with different encodings
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
        if "FSPLIT" in content_upper:
            fsplit_count += 1
        if "HEATER" in content_upper:
            heater_count += 1
        if "RADFRAC" in content_upper:
            radfrac_count += 1
        if "COMPR" in content_upper:
            compr_count += 1
        if "INFO HEAT" in content_upper:
            info_heat_count += 1
        
        total_size += len(content)

    return {
        "fsplit_count": fsplit_count,
        "heater_count": heater_count,
        "radfrac_count": radfrac_count,
        "compr_count": compr_count,
        "info_heat_count": info_heat_count,
        "total_size": total_size
    }


def read_guide_files():
    """Read heat pump distillation guide files"""
    # Try to read all markdown files
    guide_files = []
    try:
        for filename in os.listdir(GUIDE_FILES_DIR):
            if filename.endswith('.md'):
                guide_files.append(filename)
    except Exception as e:
        print(f"× Unable to read guide files directory: {e}")
        return ""
    
    guide_contents = ""
    
    for filename in guide_files:
        filepath = os.path.join(GUIDE_FILES_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                guide_contents += f"\n\n=== {filename} ===\n{content}\n"
                print(f"✓ Successfully read guide file: {filename}")
        except Exception as e:
            print(f"× Unable to read guide file {filename}: {e}")
            continue
    
    return guide_contents


def try_read_file_with_encodings(file_path):
    """Try to read a file with different encodings"""
    encodings = ['utf-8', 'gbk', 'gb18030', 'latin1', 'cp1252', 'utf-16']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                print(f"✓ Successfully read file with {encoding} encoding: {os.path.basename(file_path)}")
                return content
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"× Error reading file with {encoding} encoding: {e}")
    return None


def read_existing_process():
    """Read existing process input and report files"""
    # Read input file
    input_content = try_read_file_with_encodings(EXISTING_PROCESS_FILE)
    if input_content is None:
        print(f"× Failed to read input file with any encoding: {os.path.basename(EXISTING_PROCESS_FILE)}")
        return None, None
    
    # Read report file
    report_content = try_read_file_with_encodings(EXISTING_PROCESS_REPORT)
    if report_content is None:
        print(f"× Failed to read report file with any encoding: {os.path.basename(EXISTING_PROCESS_REPORT)}")
        return None, None
    
    return input_content, report_content


def copy_filtered_files_to_folder(heat_pump_data, excluded_large_files):
    """Copy filtered files to a dedicated folder organized by criteria"""
    try:
        # Create main filtered files directory
        if not os.path.exists(FILTERED_FILES_DIR):
            os.makedirs(FILTERED_FILES_DIR)
            print(f"✓ Created filtered files directory: {FILTERED_FILES_DIR}")
        
        # Create subdirectories for each criteria
        criteria_dirs = {}
        for criterion in ["FSPLIT", "HEATER", "RADFRAC", "COMPR", "INFO HEAT", "DESIGN-SPEC"]:
            criteria_dir = os.path.join(FILTERED_FILES_DIR, criterion)
            if not os.path.exists(criteria_dir):
                os.makedirs(criteria_dir)
            criteria_dirs[criterion] = criteria_dir
        
        # Create directory for excluded files
        excluded_dir = os.path.join(FILTERED_FILES_DIR, "EXCLUDED_LARGE_FILES")
        if not os.path.exists(excluded_dir):
            os.makedirs(excluded_dir)
        
        # Copy filtered files to appropriate subdirectories
        copied_files_count = 0
        for file_detail in heat_pump_data["file_details"]:
            source_path = file_detail["path"]
            filename = file_detail["name"]
            
            # Copy to each matching criteria directory
            for criterion in file_detail["matched_criteria"]:
                dest_path = os.path.join(criteria_dirs[criterion], filename)
                try:
                    shutil.copy2(source_path, dest_path)
                    copied_files_count += 1
                except Exception as e:
                    print(f"× Error copying {filename} to {criterion}: {e}")
        
        # Copy excluded large files
        excluded_copied = 0
        for file_data in excluded_large_files:
            source_path = file_data["path"]
            filename = file_data["name"]
            dest_path = os.path.join(excluded_dir, filename)
            try:
                shutil.copy2(source_path, dest_path)
                excluded_copied += 1
            except Exception as e:
                print(f"× Error copying excluded file {filename}: {e}")
        
        # Create summary file
        summary_path = os.path.join(FILTERED_FILES_DIR, "filtering_summary.txt")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"Heat Pump Distillation Files Filtering Summary\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"=" * 60 + "\n\n")
            
            f.write(f"Total filtered files: {heat_pump_data['file_count']}\n")
            f.write(f"Total size: {heat_pump_data['total_size']:,} characters ({heat_pump_data['total_size']/1024:.2f} KB)\n\n")
            
            f.write("Files by criteria:\n")
            for criterion, stats in heat_pump_data["criteria_stats"].items():
                if stats["files"]:
                    f.write(f"\n{criterion}:\n")
                    f.write(f"  Files: {len(stats['files'])}\n")
                    f.write(f"  Total size: {stats['total_size']:,} characters ({stats['total_size']/1024:.2f} KB)\n")
                    f.write(f"  Files list:\n")
                    for filename in stats["files"]:
                        f.write(f"    - {filename}\n")
                else:
                    f.write(f"\n{criterion}: No files found\n")
            
            if excluded_large_files:
                f.write(f"\nExcluded large files (>30KB): {len(excluded_large_files)}\n")
                for file_data in excluded_large_files:
                    f.write(f"  - {file_data['name']} ({file_data['size']/1024:.2f} KB)\n")
        
        print(f"\n" + "=" * 60)
        print("File copying results:")
        print(f"✓ Copied {len(heat_pump_data['file_details'])} filtered files to criteria subdirectories")
        print(f"✓ Copied {excluded_copied} excluded files to EXCLUDED_LARGE_FILES directory")
        print(f"✓ Created filtering summary: {summary_path}")
        print(f"✓ All files organized in: {FILTERED_FILES_DIR}")
        
        # Print directory structure
        print(f"\nDirectory structure:")
        for criterion in ["FSPLIT", "HEATER", "RADFRAC", "COMPR", "INFO HEAT", "DESIGN-SPEC"]:
            file_count = len(heat_pump_data["criteria_stats"][criterion]["files"])
            print(f"  {criterion}/: {file_count} files")
        print(f"  EXCLUDED_LARGE_FILES/: {len(excluded_large_files)} files")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"× Error creating filtered files directory: {e}")
        return False


# ====================== Main Execution ======================
os.environ["SERPER_API_KEY"] = "<your api key>"

# Get all learning files
LEARNING_FILES = []
for filepath in glob.glob(os.path.join(LEARNING_FILES_DIR, "*.inp")):
    LEARNING_FILES.append({"path": filepath, "encoding": "utf-8"})
print(f"Found {len(LEARNING_FILES)} .inp files in {LEARNING_FILES_DIR}")

# Read and classify files
heat_pump_data, excluded_large_files = read_and_classify_files(LEARNING_FILES)

# Analyze heat pump distillation files
heat_pump_stats = analyze_heat_pump_files(LEARNING_FILES)
print("\nHeat pump distillation file analysis results:")
print("-"*60)
print(f"Files containing FSPLIT keyword: {heat_pump_stats['fsplit_count']}")
print(f"Files containing HEATER keyword: {heat_pump_stats['heater_count']}")
print(f"Files containing RADFRAC keyword: {heat_pump_stats['radfrac_count']}")
print(f"Files containing COMPR keyword: {heat_pump_stats['compr_count']}")
print(f"Files containing INFO HEAT keyword: {heat_pump_stats['info_heat_count']}")
print(f"Total size of all heat pump distillation related files: {heat_pump_stats['total_size']/1024:.2f} KB")
print("-"*60)

# Print final filtering results
print("\nFinal list of files to be used:")
print("-"*60)
print(f"Heat pump distillation related files: {heat_pump_data['file_count']} files, total size {heat_pump_data['total_size']:,} characters ({heat_pump_data['total_size']/1024:.2f} KB)")

for i, file_detail in enumerate(heat_pump_data["file_details"], 1):
    criteria_str = ", ".join(file_detail["matched_criteria"])
    file_size_kb = file_detail["size"] / 1024
    print(f"{i}. {file_detail['name']} ({file_size_kb:.2f} KB) - Matches: [{criteria_str}]")

# Display criteria summary
print(f"\nSummary by filtering criteria:")
print("-" * 60)
for criterion, stats in heat_pump_data["criteria_stats"].items():
    if stats["files"]:
        print(f"{criterion}: {len(stats['files'])} files ({stats['total_size']/1024:.2f} KB)")
    else:
        print(f"{criterion}: No files")

# Display excluded large files information
if excluded_large_files:
    excluded_total_size = sum(f["size"] for f in excluded_large_files)
    print(f"\nFiles excluded due to large size (>30KB): {len(excluded_large_files)} files, total size {excluded_total_size/1024:.2f} KB")
    for i, file_data in enumerate(excluded_large_files, 1):
        if "matched_criteria" in file_data:
            criteria_str = ", ".join(file_data["matched_criteria"])
            print(f"  {i}. {file_data['name']} ({file_data['size']/1024:.2f} KB) - Would match: [{criteria_str}]")
        else:
            content_upper = file_data.get("content", "").upper()
            potential_criteria = []
            if "FSPLIT" in content_upper:
                potential_criteria.append("FSPLIT")
            if "HEATER" in content_upper:
                potential_criteria.append("HEATER")
            if "RADFRAC" in content_upper:
                potential_criteria.append("RADFRAC")
            if "COMPR" in content_upper:
                potential_criteria.append("COMPR")
            if "INFO HEAT" in content_upper:
                potential_criteria.append("INFO HEAT")
            if "DESIGN-SPEC" in content_upper:
                potential_criteria.append("DESIGN-SPEC")
            
            if potential_criteria:
                criteria_str = ", ".join(potential_criteria)
                print(f"  {i}. {file_data['name']} ({file_data['size']/1024:.2f} KB) - Would match: [{criteria_str}]")
            else:
                print(f"  {i}. {file_data['name']} ({file_data['size']/1024:.2f} KB)")

print("-"*60)

# Get learning content
heat_pump_learning_contents = heat_pump_data["contents"]

# Copy filtered files to organized folder
print("\n--- Copying filtered files to organized folder ---")
copy_success = copy_filtered_files_to_folder(heat_pump_data, excluded_large_files)

# Read heat pump distillation guide files
print("\n--- Reading heat pump distillation guide files ---")
guide_contents = read_guide_files()

# Read existing process files
print("\n--- Reading existing process files ---")
input_content, report_content = read_existing_process()

# Initialize conversation chain
memory = ConversationBufferMemory(return_messages=True)
chain = ConversationChain(llm=model, memory=memory)

# ====================== Heat Pump Distillation Model ======================
print("\n--- Generating Heat Pump Distillation model ---")

if input_content and report_content:
    print("\nGenerating heat pump distillation model...")
    
    # Heat pump distillation model generation prompt
    prompt = f"""
    You are an expert in Aspen Plus simulation and Chemical Engineering. Use your maximum knowledge and calculation capability to demonstrate your expertise. Pay attention to the accuracy of each block and stream, while keeping an eye on the whole task.
    Generate a heat pump distillation input file based on the provided example. The system should implement vapor recompression heat pump distillation for methanol-ethanol separation with energy integration.
    Please focus on the content related to the heat pump distillation system design in the existing .inp and .rep files.
    The part pinched by ** is crucial and must be strictly followed.
    Do not add any annotation or explanation text in the input file.
    Don't add any description and title in the input file.

**HEAT PUMP DISTILLATION SYSTEM CONFIGURATION:**
1.	Process design
The distillation column is the same with the previous column for methanol and ethanol separation described in the .inp file and .rep file, except for the absence of condenser. While in a traditional distillation column, the top vapour is condensed in a condenser, the vapour from the column top is compressed by a compressor in this new heat pump system to increase pressure and condensation temperature, so the vapour stream can be used to provide heat to the reboiler of the column to avoid external heat demand. A heater is connected to the compressor to provide heat to the reboiler through a "HEAT" stream and cool down the high pressure vapour to liquid, and a second heater is used to subsequently cool the fluid to the bubble point (vapour fraction 0) temperature at 1 atmosphere pressure. Then the stream is split to two streams by a FSplit, and one stream is the reflux stream to the top of the column as a traditional distillation column while the other steam is the distillate product.
2.	Detailed design of each module: there should be five blocks in the flowsheet section: Distillation Column, Compressor, First Heat Exchanger, Second heat exchanger, and a FSplit. The heat stream between the first heat exchanger and the reboiler is different from a conventional material stream, and its type is Heat stream, please refer to the official guide.
    Select the physical property method according to the existing .inp file on distillation column for methanol and ethanol separation. Remember to include the physical property database parameters accordingly.
2.1 Modified Distillation Column Configuration:
   - Set up a distillation column identical to the existing file (attached .inp file for methanol and ethanol separation) but without a condenser. So the feed stream is the same as the .rep file.
   - Use the mass flow rate and only write the mass flow rate of methanol and ethanol
   - Reduce the total number of stages and the feed stage by 1 compared to the existing configuration since the condenser is removed
   - **Because the condenser is removed, set the top pressure to the second stage pressure of the existing column. Revise the total pressure drop accordingly to the pressure drop from the second stage to the reboiler of the existing column in the. rep file.
   - **Do not forget to include the reflux stream (source: FSplit) to the top of the column and a vapour stream from the top of the column to the compressor. Ensure that the stream is included in the DEF-STREAMS section.**
   - You must add the bottom product flow rate according to the given inp file for methanol and ethanol separation. No need to specify the heat duty of the reboiler and reflux ratio
   - **There are three feed streams into the column: reflux stream above stage 1, feed described above, and heat stream to the reboiler (same grammer as the material streams in the RadFrac block and flowsheet session).**
2.2 Compressor
    - The vapor stream from the top of RADFRAC passes through a compressor that increases the pressure by 5 times the original pressure 
    - Set the efficiency of the compressor to 0.72 and the mechanical efficiency to 0.85
2.3 First heat exchanger: The compressed vapor stream from the compressor enters the first heat exchanger, where
    - Temperature is reduced to 10°C above the reboiler temperature
    - Vapor fraction is set to 0 (complete condensation)
    - Only specify two parameters of the first heat exchanger since there are only two degrees of freedom. do not specify pressure
    - The first heat exchanger has two outlets: the heat stream to the reboiler and the material stream to the second heat exchanger
2.4 Heat stream between the first heat changer and reboiler of the column
    - The heat stream is created to represent the heat flow from the first heat exchanger to the column's reboiler, so the same name should be used when specifying each block or the flowsheet section. 
    - In the flowsheet section, heat stream is taken as an out stream of the first heat exchanger (the same grammer as the material streams)
    - The heat duty of this additional heat stream should match the heat duty of the column reboiler (refer to the existing .rep file) to achieve energy integration
    - When specifying the quantity of the heat stream, use the grammer for heat streams (refer to the official guide file)
2.5	Second heat exchanger
    - The condensed stream from the first heat exchanger passes through the second heat exchanger where: Pressure is reduced to the top pressure of the modified distillation column, and Vapor fraction is set to 0 (complete condensation)
    - There are two degrees of freedom for the second heat exchanger, so only specify two parameters.
2.6 FSplit: The stream from the second heat exchanger enters an FSPLIT unit:
    - Extract and specify the reflux ratio (RR =reflux/distillate) according to the existing .rep file. Then use the reflux ratio to calculate the fraction of reflux: RR/(1+RR).
    - Use the same name for the reflux stream out of the FSPLIT unit as the reflux stream in the distillation column.
    - Only one degree of freedom for FSplit, so only specify one parameter.
2.7 Design specification 
    - Learn from the input guide files and examples to add a design specification 
    - Extract the reboiler heat duty from the existing .rep file provided in the SOURCE MATERIALS FOR REFERENCE but pay attention to the unit of the heat duty.
    - Change the compressor's pressure ratio to ensure that the heat duty of the first heater equals the negative of the value extracted from the existing .rep file provided.
    - Change the unit of the heat duty of the first heater to kW
    - Set the absolute error tolerance for the heat duty to 0.01 kW and pay attention to the unit of the heat duty.
    - Automatically set the range of the compressor's pressure ratio or outlet pressure in the form of "LIMITS"
    - Variable names in the DEFINE section must not contain underscores or special characters or numbers, use only letters
    - Only define the variable related to the heater, do not define the variable related to the distillation column
    - Use PARAM for the sentence of the heat duty of the first heater
3.	Overall settings
    - Use the SI unit system like the example .inp files
    - Pay attention to the starting, ending lines and format of the example .inp files.
    - Don't forget the semicolon at the beginning and end of the input file.
    - Use the same name for the heat stream out of the first heat exchanger as the heat stream fed into the distillation column's reboiler
    - No annotation or explanation text in the input file
    - No intermediate calculations or explanations
    - Note that if a line is too long, you can add "&" to break the line. This is what the input files do. 
    - Every "&" leads to the space of 2 characters compared to the previous line and don't add more space.
    - If there is no "&" to break the line, don't add any unnecessary space in the beginning of the line.
    - When setting the flowsheet section, figure out the inlet and outlet streams of each block and the connections between them.

SOURCE MATERIALS FOR REFERENCE:
1. Existing process files for the targeted methanol and ethanol distillation column to be reformed into the heat integration process. Note that the parameters in the report file can be used as initial guesses in the new process to converge faster:

=== EXISTING PROCESS INPUT FILE ===
{input_content}

=== EXISTING PROCESS REPORT FILE ===
{report_content}

2. Aspen Plus official guide files for relevant modules:
{guide_contents}

3. Some .inp file examples:
{chr(10).join([f"=== START OF EXAMPLE FILE: {file} ==={chr(10)}{content}{chr(10)}=== END OF EXAMPLE FILE: {file} ==={chr(10)}{chr(10)}=== NEXT EXAMPLE FILE ==={chr(10)}" for file, content in zip(heat_pump_data['file_names'], heat_pump_data['contents'][:-1])])}
=== START OF EXAMPLE FILE: {heat_pump_data['file_names'][-1]} ===
{heat_pump_data['contents'][-1]}
=== END OF EXAMPLE FILE: {heat_pump_data['file_names'][-1]} ===

Generate the complete heat pump distillation input file now:
"""

    try:
        answer_heat_pump = chain.invoke({"input": prompt})
        input_content_heat_pump = answer_heat_pump['response']

        if input_content_heat_pump:
            with open(HEAT_PUMP_FILES["input"], "w", encoding="utf-8") as f:
                f.write(input_content_heat_pump)
            print(f"Heat pump distillation input file saved to {HEAT_PUMP_FILES['input']}")

            # Run simulation
            if run_aspen_simulation(HEAT_PUMP_FILES["input"], HEAT_PUMP_FILES["report"]):
                print("Heat pump distillation simulation completed.")
            else:
                print("Heat pump distillation simulation failed.")
        else:
            print("Heat pump distillation file generation failed.")
    except Exception as e:
        print(f"Error occurred during heat pump distillation generation: {e}")
else:
    print("\nSkipping heat pump distillation generation due to missing existing process files.")

print("\nScript execution completed.")