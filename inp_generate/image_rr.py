import os
import re
import webbrowser
import requests
import json
from datetime import datetime

# API Configuration
API_KEY = "<your api key>"  # Please replace with your API key
API_URL = "<your base url>/chat/completions"

# Global variable: Store generated HTML file path
GENERATED_HTML_PATH = None

# Sensitivity Analysis Chart Generator - Automatically extracts data from Aspen Plus report files
# This script reads Aspen Plus report files and generates interactive visualization charts

def extract_data_from_rep_files():
    """Extract data from Aspen Plus report files"""
    
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Dynamically generate REP file paths based on current date
    current_date = datetime.now().strftime("%b %d").lower()  # Format like "jul 24"
    base_dir = "inp_generate/simple"
    
    # Generate file paths dynamically
    dstwu_file = os.path.join(base_dir, f"{current_date}dstsimple-general.rep")
    radfrac_file = os.path.join(base_dir, f"{current_date}radsimple-general.rep")
    
    print(f"Using DSTWU report file: {dstwu_file}")
    print(f"Using RadFrac report file: {radfrac_file}")
    
    # Check if files exist
    if not os.path.exists(dstwu_file):
        raise FileNotFoundError(f"DSTWU report file not found: {dstwu_file}")
    if not os.path.exists(radfrac_file):
        raise FileNotFoundError(f"RadFrac report file not found: {radfrac_file}")
    
    # Extract minimum reflux ratio from DSTWU file
    with open(dstwu_file, 'r', encoding='utf-8') as f:
        dstwu_content = f.read()
        
    # Extract minimum reflux ratio
    min_rr_match = re.search(r'MINIMUM REFLUX RATIO\s+(\d+\.?\d*)', dstwu_content)
    min_reflux_ratio = float(min_rr_match.group(1))
    print(f"Extracted minimum reflux ratio: {min_reflux_ratio}")
    
    # Extract S1 sensitivity analysis data to get RadFrac minimum reflux ratio
    with open(radfrac_file, 'r', encoding='utf-8') as f:
        radfrac_content = f.read()
        
    # Extract S1 sensitivity analysis RR1 minimum value
    s1_start = radfrac_content.find('SENSITIVITY BLOCK:  S1 (CONTINUED)')
    s1_section = radfrac_content[s1_start:s1_start+20000]  # Get a large section
    
    # Find all RR1 values from S1 analysis
    rr1_pattern = r'!\s*\d+\.\d+\s*!\s*\d+\.\d+\s*!\s*(\d+\.\d+)\s*!'
    rr1_matches = re.findall(rr1_pattern, s1_section)
    
    # Convert to float and filter out convergence failures (10.0000)
    valid_rr1 = [float(x) for x in rr1_matches if float(x) < 10.0]
    radfrac_min_rr = min(valid_rr1)
    print(f"Extracted RadFrac minimum reflux ratio (S1): {radfrac_min_rr}")
    
    # Extract S2 sensitivity analysis data from RADFRAC file
    # Find S2 sensitivity analysis section
    s2_start = radfrac_content.find('SENSITIVITY BLOCK:  S2')
    
    # Extract S2 analysis table data
    # Find table start marker
    table_start = radfrac_content.find('!============!============!============!============!', s2_start)
    
    # Extract all data rows until sensitivity analysis ends
    table_section = radfrac_content[table_start:]
    
    # Parse data rows - S2 analysis has only 4 columns: NSTAGE, FEED STAGE, RR2, QREB
    data_pattern = r'!\s*(\d+\.?\d*)\s*!\s*(\d+\.?\d*)\s*!\s*(\d+\.?\d*)\s*!\s*([+-]?\d+\.?\d*[Ee]?[+-]?\d*)\s*!'
    data_matches = re.findall(data_pattern, table_section)
    
    # Organize data by NSTAGE
    stage_data = {}
    
    def parse_scientific_notation(value_str):
        """Parse ASPEN special format scientific notation"""
        # Handle format like 1.3863+05
        if ('+' in value_str or '-' in value_str[1:]) and 'E' not in value_str.upper():
            for i, char in enumerate(value_str[1:], 1):
                if char in '+-':
                    return float(value_str[:i] + 'E' + value_str[i:])
        return float(value_str)
    
    for match in data_matches:
        nstage = int(float(match[0]))
        feed_stage = int(float(match[1]))
        rr = float(match[2])
        reb_duty = parse_scientific_notation(match[3])  # WATT
        
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
    
    return min_reflux_ratio, radfrac_min_rr, stage_data, nstages


def generate_html_with_ai(min_reflux_ratio, radfrac_min_rr, stage_data, nstages):
    """Generate HTML content using AI (OpenRouter API)"""
    
    # Convert extracted data to JavaScript format - filter out invalid data points
    js_nstages = []
    
    # Convert each stage's data to the required format, filtering out RR >= 10.0 and constant RR values
    for nstage in nstages:
        if nstage in stage_data:
            stage_info = stage_data[nstage]
            # Filter out invalid data points (RR >= 10.0 indicates convergence failure)
            valid_indices = [i for i, rr in enumerate(stage_info['rr']) if rr < 10.0]
            
            if valid_indices:  # Only include stages with valid data
                # Get valid RR values
                valid_rr = [stage_info['rr'][i] for i in valid_indices]
                
                # Find the last meaningful data point (ensure last point <= first point)
                first_valid_rr = valid_rr[0]  # First valid RR value
                last_meaningful_index = 0  # Start with first point
                
                for i in range(len(valid_rr)):
                    if valid_rr[i] <= first_valid_rr:  # Ensure RR doesn't increase above first value
                        last_meaningful_index = i
                    else:
                        break  # Stop when RR exceeds first value
                
                # Use only meaningful data points
                meaningful_indices = valid_indices[:last_meaningful_index + 1]
                
                # Only include stages with at least 5 data points
                if len(meaningful_indices) >= 5:
                    js_nstages.append({
                        'nt': stage_info['nt'],
                        'feed_stages': [stage_info['feed_stage'][i] for i in meaningful_indices],
                        'rr': [stage_info['rr'][i] for i in meaningful_indices],
                        'reb': [stage_info['rebduty'][i] for i in meaningful_indices]
                    })

    # Fix solution: Maintain high precision, reduce AI processing complexity
    nstages_high_precision = []
    for stage_info in js_nstages:
        stage_data = {
            'nt': stage_info['nt'],
            'feed_stages': stage_info['feed_stages'],
            'rr': [round(x, 4) for x in stage_info['rr']],  # Keep 4 decimal places
            'reb': [int(round(x)) for x in stage_info['reb']]  # Keep as integers to match original format
        }
        nstages_high_precision.append(stage_data)
    
    # Use simpler data format, avoid AI over-simplification
    compact_data_str = json.dumps(nstages_high_precision, separators=(',', ':'))
    
    # Print data filtering summary
    print(f"Data filtering summary:")
    print(f"  Original stages: {len(nstages)}")
    print(f"  Valid stages after filtering: {len(nstages_high_precision)}")
    for stage_data in nstages_high_precision:
        print(f"    Nt {stage_data['nt']}: {len(stage_data['feed_stages'])} valid data points (RR <= first_valid_rr, >=5 points)")
    
    # Calculate dynamic axis ranges based on actual data
    all_feed_stages = []
    all_rr_values = []
    all_reb_values = []
    
    for stage_data in nstages_high_precision:
        all_feed_stages.extend(stage_data['feed_stages'])
        all_rr_values.extend(stage_data['rr'])
        all_reb_values.extend(stage_data['reb'])
    
    # Calculate ranges based on actual valid data points only
    x_min, x_max = min(all_feed_stages), max(all_feed_stages)
    x_padding = (x_max - x_min) * 0.05  # 5% padding for x-axis
    x_range = [x_min, x_max + x_padding]  # Add 5% padding to x-axis maximum
    
    rr_min, rr_max = min(all_rr_values), max(all_rr_values)
    rr_padding = (rr_max - rr_min) * 0.1  # 10% padding
    rr_range = [rr_min - rr_padding, rr_max + rr_padding]
    
    reb_min, reb_max = min(all_reb_values), max(all_reb_values)
    reb_padding = (reb_max - reb_min) * 0.1  # 10% padding
    reb_range = [reb_min - reb_padding, reb_max + reb_padding]
    
    print(f"  Dynamic ranges calculated:")
    print(f"    X-axis (Feed stage): {x_range[0]:.1f} - {x_range[1]:.1f} (with 5% padding)")
    print(f"    Y-axis (Reflux ratio): {rr_range[0]:.4f} - {rr_range[1]:.4f}")
    print(f"    Y-axis (Reboiler): {reb_range[0]:.0f} - {reb_range[1]:.0f}")
    
    # Calculate reference lines values
    dstwu_min_rr = min_reflux_ratio
    radfrac_min_rr_s1 = radfrac_min_rr
    radfrac_min_rr_12x = radfrac_min_rr * 1.2
    
    # Calculate precise annotation positions for perfect alignment
    # Position annotations inside the chart area with proper spacing
    annotation_x = x_min + (x_max - x_min) * 0.02  # 2% from left edge, inside chart
    
    # Calculate annotation y-positions with consistent spacing
    annotation_spacing = 0.2  # Spacing from reference lines
    
    # Position annotations relative to their lines, ensuring they stay within bounds
    dstwu_annotation_y = min(dstwu_min_rr + annotation_spacing, rr_range[1] - 0.1)  # Above the line
    radfrac_annotation_y = max(radfrac_min_rr_s1 - annotation_spacing, rr_range[0])  # Below the line
    radfrac_12x_annotation_y = max(radfrac_min_rr_12x - annotation_spacing, rr_range[0])  # Below the line
    
    
    prompt = f"""
Generate a complete HTML file for Aspen Plus sensitivity analysis visualization - REFLUX RATIO CHART ONLY.
The part pinched by ** is crucial and must be strictly followed.
Although the AI can automatically generate the chart, it also needs the requirements below to beautify the chart.

1. DATA FORMAT AND INPUT
1.1. Data Format: Each stage has variable number of data points with corresponding feed_stages, rr (reflux ratios), and reb (reboiler heat duties).
1.2. Data: {compact_data_str}

2. DATA PROCESSING REQUIREMENTS
2.1. Filter out all data points where reflux ratio (rr) >= 10.0 (these indicate convergence failures)
2.2. Filter out data points where reflux ratio exceeds the first valid data point value
2.3. Only plot valid data points where rr < 10.0 and rr <= first_valid_rr
2.4. Only include stages with at least 5 valid data points for meaningful analysis
2.5. Each stage may have different valid feed stage ranges
2.6. Use the exact feed stage numbers from the data, do not assume sequential numbering

3. AXIS CONFIGURATION
3.1. X-axis (Feed stage): {x_range[0]:.1f} to {x_range[1]:.1f} (with 5% padding above max data point)
3.2. X-axis tick spacing: 2 (show ticks at intervals of 2)
3.3. **X-axis tick direction: inside (ticks pointing inward)**
3.4. Y-axis (Reflux ratio): {rr_range[0]:.4f} to {rr_range[1]:.4f}
3.5. **Y-axis tick direction: inside (ticks pointing inward)**

4. REFERENCE LINES
4.1. Blue (#1f4e79): y={radfrac_min_rr_s1} (RadFrac R_min) - horizontal line across full chart width
4.2. Black (#2f2f2f): y={dstwu_min_rr} (DSTWU R_min) - horizontal line across full chart width
4.3. Gray (#808080): y={radfrac_min_rr_12x} (1.2×RadFrac R_min) - horizontal line across full chart width

5. REFERENCE LINE STYLE
5.1. Use dashed lines with dash pattern: [10, 5] (10px dash, 5px gap)
5.2. Line width: 3px for all reference lines
5.3. Extend lines across the full chart width (from x_min to x_max)
5.4. Use consistent dash pattern for all three reference lines

6. ANNOTATIONS
6.1. CRITICAL: All three reference line annotations MUST be perfectly aligned at exactly x={annotation_x:.2f}
6.2. DSTWU: x={annotation_x:.2f}, y={dstwu_annotation_y:.4f}, text='R<sub>min</sub> (DSTWU)', font_size=20px, xanchor='left'
6.3. RadFrac: x={annotation_x:.2f}, y={radfrac_annotation_y:.4f}, text='R<sub>min</sub> (RadFrac)', font_size=20px, xanchor='left'
6.4. 1.2×RadFrac: x={annotation_x:.2f}, y={radfrac_12x_annotation_y:.4f}, text='1.2×R<sub>min</sub> (RadFrac)', font_size=20px, xanchor='left'
6.5. All annotations use identical x-coordinate ({annotation_x:.2f}) and xanchor='left' for perfect vertical alignment
6.6. Position annotations inside chart area (not outside boundaries)
6.7. Use smaller font size (20px) to prevent overflow

7. CHART REQUIREMENTS
7.1. ONLY ONE PLOT: Reflux ratio vs Feed stage
7.2. Use Plotly.js for interactive charts
7.3. Plot ONLY valid data points (rr < 10.0) for each Nt configuration
7.4. Professional styling: Arial font, clean layout, A4 print-friendly
7.5. Chart dimensions: 1000x800px (single chart)
7.6. Use the provided dynamic axis ranges (see section 3 above)
7.7. Color scheme: blues/oranges/greens for different Nt configurations
7.8. Use lines+markers mode for better visualization
7.9. Add hover templates showing Nt number, feed stage, and reflux ratio values
7.10. CRITICAL: X-axis title must be "Feed stage" (only first letter capitalized)
7.11. CRITICAL: Y-axis title must be "Reflux ratio" (only first letter capitalized)
7.12. CRITICAL: All reference line annotations must be perfectly aligned at x={x_min:.1f} with xanchor='right'

8. VISUALIZATION IMPROVEMENTS
8.1. Increase marker size to 11px for better visibility
8.2. Use thicker lines (width: 5.5) to separate curves clearly
8.3. Add colored borders around markers for better contrast
8.4. Use larger font sizes: axis titles 48px, tick labels 42px, annotations 30px
8.5. Maintain aspect ratio close to 1:1 for better readability
8.6. Use spline line shape for smoother curves
8.7. Add colored circle markers with colored borders to highlight minimum points
8.8. Use hollow circles for minimum points of each line, solid colored circles for other data points
8.9. Use spline curves that connect all data points but do not pass through marker centers
8.10. Lines should connect smoothly between data points while avoiding marker centers
8.11. Ensure proper spacing between curves for clarity
8.12. Use professional color palette with good contrast
8.13. Add minimum point detection and highlighting
8.14. For each line, find the local minimum point (point that is smaller than both its neighbors)
8.15. Use the following algorithm to detect local minimum: for each valid data point, check if it is smaller than both the previous and next points
8.16. Only highlight the first local minimum found for each line (break after finding the first one)
8.17. Use proper margins: left 150px, right 100px, top 80px, bottom 120px
8.18. Remove grid lines for cleaner appearance
8.19. **Use inside ticks with proper tick length and width (ticks pointing inward)**

9. DATA FILTERING LOGIC
9.1. For each stage, create arrays of valid data points:
9.2. validFeedStages = feed_stages where corresponding rr < 10.0 AND rr <= first_valid_rr
9.3. validRR = rr values where rr < 10.0 AND rr <= first_valid_rr
9.4. Stop plotting when RR exceeds the first valid data point value
9.5. Only include stages with at least 5 valid data points

10. LOCAL MINIMUM DETECTION
10.1. For each line, implement local minimum detection:
10.2. Iterate through valid data points (excluding first and last points)
10.3. For each point at index j, check if validRR[j] < validRR[j-1] AND validRR[j] < validRR[j+1]
10.4. If true, mark this as the local minimum and break (find only the first local minimum)
10.5. Use this local minimum point for special highlighting (hollow circle)

11. STYLE SPECIFICATIONS
11.1. Font family: Arial throughout
11.2. Chart background: white
11.3. Paper background: white
11.4. Line colors: use distinct colors for each Nt configuration, avoid similar shades
11.5. Marker style: solid circles (size 11) with colored fill and white borders for regular points, hollow circles (size 15, empty fill) with colored borders for minimum points
11.6. Line style: spline curves with width 5.5, connect all data points smoothly while avoiding marker centers
11.7. Axis lines: 3.5px width, dark color (#2f2f2f)
11.8. **Tick style: inside ticks (pointing inward), 10px length, 3.5px width**
11.9. No grid lines for clean appearance
11.10. No chart border/frame - only show X and Y axes
11.11. Proper spacing between curves to avoid overlap

12. EXAMPLE MARKER STYLES (JavaScript)
12.1. Regular data points - solid colored circles with white borders:
marker: {{
    size: 11,
    color: colors[i],
    line: {{
        color: 'white',
        width: 3
    }}
}}

12.2. Minimum points - hollow circles with colored borders:
marker: {{
    size: 15,
    color: 'white',
    line: {{
        color: colors[i],
        width: 3
    }}
}}

12.3. Spline curves with proper marker styling to avoid lines passing through centers
12.4. Use white borders around markers to create visual separation from lines

13. EXAMPLE LINE STYLE (JavaScript)
13.1. Spline curves that connect data points without passing through marker centers:
line: {{
    color: colors[i],
    width: 5.5,
    shape: 'spline'
}}

Output complete HTML with embedded CSS/JavaScript, ready to run in browser.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Use your selected model
    model_name = "<your model>"
    
    data = {
        "model": model_name,  
        "messages": [
            {
                "role": "system",
                "content": "You are an expert HTML/JavaScript generator for scientific data visualization. Create professional Plotly.js charts with precise data handling. CRITICAL: Always filter out data points where reflux ratio >= 10.0 as these indicate convergence failures. Also filter out data points where reflux ratio exceeds the first valid data point value. Only plot valid data points where RR <= first_valid_rr. Only include stages with at least 5 valid data points. Use exact coordinates and colors as specified. IMPORTANT: Create high-quality visualizations with large fonts, thick lines, clear markers, and proper spacing. CRITICAL: Use 'Nt' as the label prefix instead of 'Stage' in all legends, hover text, and annotations. CRITICAL: X-axis range is optimized to target maximum value around 32 for better visualization. CRITICAL: Use smaller font size (24px) for reference line annotations. CRITICAL: Use hollow circles (size 15, empty fill) for minimum points of each line, solid colored circles (size 11) with white borders for other data points. CRITICAL: Use spline curves that connect data points smoothly without passing through marker centers. CRITICAL: Implement local minimum detection for each line - find the first point that is smaller than both its neighbors. CRITICAL: All three reference line annotations MUST be perfectly aligned at the exact same x-coordinate with xanchor='left' - this is absolutely essential for visual consistency. The x-coordinate for all three annotations must be identical and positioned inside the chart area. CRITICAL: X-axis title must be 'Feed stage' (only first letter capitalized). CRITICAL: Y-axis title must be 'Reflux ratio' (only first letter capitalized). CRITICAL: Use inside ticks for both X and Y axes (ticks pointing inward). Generate complete, production-ready HTML files. ONLY CREATE THE REFLUX RATIO CHART - DO NOT CREATE THE REBOILER DUTY CHART."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "max_tokens": 32000,  # Increased for complete HTML output
        "temperature": 0.0  # Lower temperature to ensure precision
    }
    
    print(f"Using Grok 3 for HTML generation (simplified prompt)...")
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
    
    print(f"Generated HTML length: {len(html_content)} characters")
    print("AI HTML preview:", html_content[:200] + "..." if len(html_content) > 200 else html_content)
    
    return html_content



def save_and_open_html(html_content):
    """Save HTML content to file and open in browser"""
    global GENERATED_HTML_PATH
    
    # Use the same base directory as extract_data_from_rep_files function
    base_dir = "inp_generate/simple"
    output_dir = os.path.join(base_dir, "image")
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename without timestamp
    filename = "sensitivity_analysis.html"
    filepath = os.path.join(output_dir, filename)
    
    # Write content to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML file saved to: {filepath}")
    
    # Set global variable
    GENERATED_HTML_PATH = filepath
    
    # Open in default browser
    webbrowser.open(f'file://{filepath}')
    
    return filepath

def main():
    print("Extracting data from Aspen Plus report files...")
    min_reflux_ratio, radfrac_min_rr, stage_data, nstages = extract_data_from_rep_files()
    
    print("Generating HTML visualization using AI...")
    html_content = generate_html_with_ai(min_reflux_ratio, radfrac_min_rr, stage_data, nstages)
    
    print("Saving and opening HTML file...")
    save_and_open_html(html_content)
    print("Done!")

if __name__ == "__main__":
    main()