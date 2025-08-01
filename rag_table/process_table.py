
import base64
import os
from openai import OpenAI
import re

# --- Configuration ---
# Use the more powerful Claude 3.5 Sonnet model to improve recognition accuracy
api_key = "<your api key>"
base_url = "<your base url>"
vision_model = "<your model>"

# Create OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    default_headers={"HTTP-Referer": "http://localhost", "X-Title": "RAG-Modular-Project"},
)

# List of image file paths
IMAGE_PATHS = [
    "web_content/gxt_spec_table_part1.jpg",
    "web_content/gxt_spec_table_part2.jpg"
]
# Output directory and filename
OUTPUT_DIR = "parsed_Web_PDF"
OUTPUT_MD_FILE = "gxt_specification_table_parsed.md"

# --- Function Definitions ---
def encode_image_to_base64(image_path, verbose=True):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        if verbose:
            print(f"Error: Image file not found at path: {image_path}")
        return None

def image_to_markdown_table(base64_image, prompt, image_name, verbose=True):
    if verbose:
        print(f"Parsing {image_name} with Claude 3.5 Sonnet, please wait...")
    try:
        response = client.chat.completions.create(
            model=vision_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=4000,
            temperature=0,
        )
        if verbose:
            print(f"Model successfully parsed {image_name}!")
        content = response.choices[0].message.content
        
        # Stricter cleaning logic
        if "```markdown" in content:
            # Extract markdown code block
            start = content.find("```markdown") + 11
            end = content.rfind("```")
            if end > start:
                content = content[start:end].strip()
        elif "```" in content:
            # Extract regular code block
            start = content.find("```") + 3
            end = content.rfind("```")
            if end > start:
                content = content[start:end].strip()
        
        # Further cleaning: only keep table rows (lines starting with |)
        lines = content.split('\n')
        table_lines = []
        for line in lines:
            line = line.strip()
            if line.startswith('|') and line.endswith('|'):
                table_lines.append(line)
        
        if table_lines:
            return '\n'.join(table_lines)
        else:
            # If no standard table rows are found, return the original cleaned content
            return content.strip()
            
    except Exception as e:
        if verbose:
            print(f"An error occurred while calling the API: {e}")
        return None

def simple_merge_tables(table1, table2, verbose=True):
    if not table1 or not table2:
        return table1 or table2
    
    if verbose:
        print("Starting to simply merge two tables...")
    
    # Split tables into lines
    lines1 = [line.strip() for line in table1.strip().split('\n') if line.strip()]
    lines2 = [line.strip() for line in table2.strip().split('\n') if line.strip()]
    
    if len(lines1) < 2 or len(lines2) < 2:
        if verbose:
            print("Warning: Incomplete table format.")
        return table1 + "\n\n" + table2
    
    # Extract headers
    header1_parts = [part.strip() for part in lines1[0].split('|') if part.strip()]
    header2_parts = [part.strip() for part in lines2[0].split('|') if part.strip()]
    
    # Merge headers: the first column is the parameter name, followed by all models
    param_col = header1_parts[0] if header1_parts else "Parameter"
    all_models = header1_parts[1:] + header2_parts[1:]
    
    # Build new header
    merged_header = "| " + param_col + " | " + " | ".join(all_models) + " |"
    separator = "|" + "------|" * (len(all_models) + 1)
    
    # Merge data rows
    merged_rows = []
    
    # Get data rows (skip header and separator)
    data1 = lines1[2:] if len(lines1) > 2 else []
    data2 = lines2[2:] if len(lines2) > 2 else []
    
    # Ensure consistent row count, take the smaller value
    min_rows = min(len(data1), len(data2))
    
    for i in range(min_rows):
        # Parse row data
        parts1 = [part.strip() for part in data1[i].split('|') if part.strip()]
        parts2 = [part.strip() for part in data2[i].split('|') if part.strip()]
        
        if not parts1 or not parts2:
            continue
        
        # Take the parameter name from the first table
        param_name = parts1[0]
        
        # Merge data: data from table1 + data from table2 (skipping parameter column)
        all_data = parts1[1:] + parts2[1:]
        
        merged_row = "| " + param_name + " | " + " | ".join(all_data) + " |"
        merged_rows.append(merged_row)
    
    # Build the final table
    final_table = "\n".join([merged_header, separator] + merged_rows)
    if verbose:
        print(f"Table merge complete. Total of {len(all_models)} models and {len(merged_rows)} data rows.")
    
    return final_table

def save_to_markdown(content, file_name, verbose=True):
    try:
        # Ensure the output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Build the full file path
        file_path = os.path.join(OUTPUT_DIR, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        if verbose:
            print(f"Table successfully saved to: {file_path}")
        return file_path
    except IOError as e:
        if verbose:
            print(f"An error occurred while saving the file: {e}")
        return None

def main(verbose=True):

    prompt_text = """
    Extract the table from this image into a Markdown format.
    """

    # A stricter prompt that only requests table output
#     prompt_text = """
# Please analyze this GXT cooling tower specification table image and extract all data.

# **Output requirements:**
# Only output the pure Markdown table, without any explanatory text.
# Format: | Parameter Name | Model 1 | Model 2 | ... |

# Please ensure accurate number recognition, paying special attention to decimal point placement and distinguishing between similar digits.
# """

    extracted_tables = []

    # Process each image
    for image_path in IMAGE_PATHS:
        if verbose:
            print(f"\n--- Processing image: {os.path.basename(image_path)} ---")
        base64_image_data = encode_image_to_base64(image_path, verbose=verbose)
        if not base64_image_data:
            continue

        markdown_table = image_to_markdown_table(
            base64_image_data, 
            prompt_text, 
            os.path.basename(image_path),
            verbose=verbose
        )
        
        if markdown_table:
            extracted_tables.append(markdown_table)

    # Merge results
    if len(extracted_tables) >= 2:
        final_table = simple_merge_tables(extracted_tables[0], extracted_tables[1], verbose=verbose)
        if final_table:
            save_to_markdown(final_table, OUTPUT_MD_FILE, verbose=verbose)
            if verbose:
                print("\n✅ Table extraction and merging complete!")

    elif len(extracted_tables) == 1:
        save_to_markdown(extracted_tables[0], OUTPUT_MD_FILE, verbose=verbose)
        if verbose:
            print("Only one table was successfully extracted.")
    else:
        if verbose:
            print("Failed to extract any tables.")

if __name__ == "__main__":
    main() 