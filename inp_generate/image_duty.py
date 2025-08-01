import os
import re
import webbrowser
import requests
import json
import subprocess
import sys
from datetime import datetime

# API Configuration
API_KEY = "<your api key>"
API_URL = "<your base url>"

# Define base directory path (same as other files)
BASE_DIR = "inp_generate/simple"
OUTPUT_DIR = os.path.join(BASE_DIR, "image")

def get_template_html_path():
    """Get the HTML template file path directly from the image directory"""
    try:
        # Look for existing sensitivity_analysis.html file
        template_path = os.path.join(OUTPUT_DIR, "sensitivity_analysis.html")
        
        if os.path.exists(template_path):
            print(f"Using existing template file: {template_path}")
            return template_path
        else:
            # If not found, try to find any HTML file in the image directory
            html_files = [f for f in os.listdir(OUTPUT_DIR) 
                         if f.endswith('.html')]
            
            if html_files:
                # Use the first HTML file found
                template_path = os.path.join(OUTPUT_DIR, html_files[0])
                print(f"Using available HTML file as template: {template_path}")
                return template_path
            else:
                raise FileNotFoundError(f"No HTML template files found in {OUTPUT_DIR}")
        
    except Exception as e:
        print(f"Error getting template HTML path: {e}")
        raise

def extract_data_from_rep_files():
    """Extract S2 sensitivity analysis data from Aspen Plus report files"""
    
    # Dynamically generate REP file path based on current date
    current_date = datetime.now().strftime("%b %d").lower()  # Format like "jul 24"
    base_dir = "inp_generate/simple"
    
    # Generate file path dynamically
    radfrac_file = os.path.join(base_dir, f"{current_date}radsimple-general.rep")
    
    print(f"Using RadFrac report file: {radfrac_file}")
    
    # Check if file exists
    if not os.path.exists(radfrac_file):
        raise FileNotFoundError(f"RadFrac report file not found: {radfrac_file}")
    
    # Extract S2 sensitivity analysis data from RADFRAC file
    with open(radfrac_file, 'r', encoding='utf-8') as f:
        radfrac_content = f.read()
        
    # Find S2 sensitivity analysis section
    s2_start = radfrac_content.find('SENSITIVITY BLOCK:  S2')
    
    # Extract S2 analysis table data
    table_start = radfrac_content.find('!============!============!============!============!', s2_start)
    table_section = radfrac_content[table_start:]
    
    # Extract unit information from the table header
    unit_match = re.search(r'!.*!.*!.*!\s*(\w+)\s*!', table_section)
    heat_duty_unit = unit_match.group(1) if unit_match else "WATT"
    print(f"Extracted heat duty unit from rep file: {heat_duty_unit}")
    
    # Parse data rows - S2 analysis has 4 columns: NSTAGE, FEED STAGE, RR2, QREB
    data_pattern = r'!\s*(\d+\.?\d*)\s*!\s*(\d+\.?\d*)\s*!\s*(\d+\.?\d*)\s*!\s*([+-]?\d+\.?\d*[Ee]?[+-]?\d*)\s*!'
    data_matches = re.findall(data_pattern, table_section)
    
    # Organize data by NSTAGE
    stage_data = {}
    
    def parse_scientific_notation(value_str):
        """Parse ASPEN special format scientific notation"""
        if ('+' in value_str or '-' in value_str[1:]) and 'E' not in value_str.upper():
            for i, char in enumerate(value_str[1:], 1):
                if char in '+-':
                    return float(value_str[:i] + 'E' + value_str[i:])
        return float(value_str)
    
    for match in data_matches:
        nstage = int(float(match[0]))
        feed_stage = int(float(match[1]))
        rr = float(match[2])
        reb_duty = parse_scientific_notation(match[3])
        
        # Skip RR = 10 data points (indicates convergence failure)
        if rr >= 10.0:
            continue
            
        if nstage not in stage_data:
            stage_data[nstage] = {
                'nt': nstage,
                'feed_stage': [],
                'rr': [],
                'rebduty': []
            }
        
        stage_data[nstage]['feed_stage'].append(feed_stage)
        stage_data[nstage]['rr'].append(rr)
        stage_data[nstage]['rebduty'].append(reb_duty)
    
    # Get all unique NSTAGE values
    nstages = sorted(stage_data.keys())
    print(f"Found NSTAGE values: {nstages}")
    
    return stage_data, nstages, heat_duty_unit

def convert_heat_duty_to_kw(reb_duty_watt):
    """Convert heat duty from WATT to kW"""
    return reb_duty_watt / 1000.0

def generate_html_with_ai(stage_data, nstages, heat_duty_unit):
    """Generate HTML content using AI (OpenRouter API)"""
    
    # Convert extracted data to JavaScript format - filter out invalid data points
    js_nstages = []
    
    for nstage in nstages:
        if nstage in stage_data:
            stage_info = stage_data[nstage]
            # Filter out invalid data points (RR >= 10.0 indicates convergence failure)
            valid_indices = [i for i, rr in enumerate(stage_info['rr']) if rr < 10.0]
            
            if valid_indices:
                valid_rr = [stage_info['rr'][i] for i in valid_indices]
                
                # Find the last meaningful data point (ensure last point <= first point)
                first_valid_rr = valid_rr[0]
                last_meaningful_index = 0
                
                for i in range(len(valid_rr)):
                    if valid_rr[i] <= first_valid_rr:
                        last_meaningful_index = i
                    else:
                        break
                
                # Use only meaningful data points
                meaningful_indices = valid_indices[:last_meaningful_index + 1]
                
                # Only include stages with at least 5 data points
                if len(meaningful_indices) >= 5:
                    # Convert heat duty from WATT to kW for plotting
                    reb_duty_kw = [convert_heat_duty_to_kw(stage_info['rebduty'][i]) for i in meaningful_indices]
                    
                    js_nstages.append({
                        'nt': stage_info['nt'],
                        'feed_stages': [stage_info['feed_stage'][i] for i in meaningful_indices],
                        'rr': [stage_info['rr'][i] for i in meaningful_indices],
                        'reb': reb_duty_kw  # Now in kW
                    })

    # Format data for AI processing
    nstages_high_precision = []
    for stage_info in js_nstages:
        stage_data = {
            'nt': stage_info['nt'],
            'feed_stages': stage_info['feed_stages'],
            'rr': [round(x, 4) for x in stage_info['rr']],
            'reb': [round(x, 2) for x in stage_info['reb']]  # Round to 2 decimal places for kW
        }
        nstages_high_precision.append(stage_data)
    
    compact_data_str = json.dumps(nstages_high_precision, separators=(',', ':'))
    
    # Get template file path and read content
    template_file_path = get_template_html_path()
    try:
        with open(template_file_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file not found at: {template_file_path}")
    
    # Calculate Y-axis range based on actual data
    all_reb_values = []
    
    for stage_data in nstages_high_precision:
        all_reb_values.extend(stage_data['reb'])
    
    reb_min, reb_max = min(all_reb_values), max(all_reb_values)
    # Extend Y-axis upward to provide space for legend at top, but keep it compact
    reb_padding = (reb_max - reb_min) * 0.15  # Reduced padding for more compact layout
    reb_range = [reb_min - reb_padding, reb_max + reb_padding * 1.2]  # Less space at top for tighter layout
    
    # Use template to generate prompt
    prompt = f"""
Use the following HTML template as a base to generate a reboiler heat duty chart.
The part pinched by ** is crucial and must be strictly followed.

Template file content:
{template_content}

Data:
{compact_data_str}

Requirements:

1. DATA PROCESSING:
   1.1. Filter out data points where RR >= 10.0 (indicates convergence failure)
   1.2. Only include stages with at least 5 valid data points
   1.3. Convert heat duty values from {heat_duty_unit} to kW for plotting
   1.4. Use X-axis range that matches the template exactly, Y-axis {reb_range[0]:.2f} to {reb_range[1]:.2f} kW

2. CHART GENERATION:
   2.1. Generate the reboiler heat duty chart (Reboiler heat duty vs Feed Stage)
   2.2. Replace the data in the template with the provided data
   2.3. Maintain the template's style and layout
   2.4. Detect and mark local minimum points for each line (hollow circles)
   2.5. Update the Y-axis title to show "Reboiler heat duty (kW)"

3. AXIS FORMATTING:
   3.1. Use proper margins: left 180px, right 10px, top 100px, bottom 120px (reduced top margin for compact layout)
   3.2. Y-axis should start exactly at the minimum value to align with X-axis
   3.3. X-axis range must match the template format exactly
   3.4. Remove any extra tick marks beyond the data range
   3.5. Ensure Y-axis minimum aligns properly with X-axis baseline
   3.6. Ensure all data points are visible and not cut off by axis limits
   3.7. **CRITICAL: X-axis range must match the template format to maintain complete consistency**
   3.8. Chart dimensions: 1000x800px (single chart)

4. LEGEND POSITIONING:
   4.1. Move stage labels (Nt=xx) to the TOP of the chart as a horizontal legend within Y-axis range
   4.2. Position legend at the TOP of the chart, within the Y-axis range, close to the highest data points
   4.3. Position legend just above the highest data points to minimize empty space

5. LEGEND FORMATTING (CRITICAL):
   5.1. Font size: 22px
   5.2. Font weight: bold
   5.3. Font family: Arial, sans-serif
   5.4. Text color: match the line color
   5.5. Background: transparent
   5.6. Border: none
   5.7. Padding: 6px between legend items
   5.8. Format: "Nt=xx" (e.g., "Nt=21", "Nt=22")
   5.9. Horizontal spacing: 15px between legend items
   5.10. Make the legend more prominent and easier to read
   5.11. **CRITICAL: Arrange legend items in equal rows with exactly the same number of items per row**
   5.12. **CRITICAL: Ensure each row has the same number of items for uniform layout**
   5.13. **CRITICAL: Do not allow uneven distribution - all rows must have the same number of items to beautify the image**

Please generate a complete HTML file."""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    model_name = "<your model>"
    
    data = {
        "model": model_name,  
        "messages": [
            {
                "role": "system",
                "content": "You are an HTML/JavaScript expert specializing in scientific data visualization. Use Plotly.js to create professional reboiler heat duty charts. Filter out data points where RR >= 10.0, only include valid data. Generate complete HTML files. Heat duty values are in kW."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "max_tokens": 32000,
        "temperature": 0.0
    }
    
    response = requests.post(API_URL, headers=headers, json=data, timeout=180)
    
    result = response.json()
    ai_response = result['choices'][0]['message']['content'].strip()
    
    # Clean response content - Extract HTML code
    if '```html' in ai_response:
        html_content = ai_response.split('```html')[1].split('```')[0].strip()
    elif '```' in ai_response:
        html_content = ai_response.split('```')[1].split('```')[0].strip()
    else:
        html_content = ai_response
    
    return html_content

def save_and_open_html(html_content):
    """Save HTML content to file and open in browser"""
    output_dir = OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    
    filename = "reboiler_heat_duty_analysis.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML file saved to: {filepath}")
    webbrowser.open(f'file://{filepath}')
    
    return filepath

def main():
    print("Extracting S2 sensitivity analysis data...")
    stage_data, nstages, heat_duty_unit = extract_data_from_rep_files()
    
    print(f"Converting heat duty from {heat_duty_unit} to kW for plotting...")
    print("Generating HTML visualization...")
    html_content = generate_html_with_ai(stage_data, nstages, heat_duty_unit)
    
    print("Saving and opening HTML file...")
    save_and_open_html(html_content)
    print("Done!")

if __name__ == "__main__":
    main()


