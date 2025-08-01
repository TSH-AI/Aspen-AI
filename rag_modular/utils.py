"""
utils.py
Common utility functions such as file checking, text processing, logging, async concurrency, etc.
"""

from pathlib import Path
import re
import asyncio
from typing import List, Tuple, Any

def ensure_dir_exists(path: Path):
    """
    Ensure directory exists, create if it doesn't exist
    Args:
        path (Path): Directory path
    """
    path.mkdir(parents=True, exist_ok=True)

def file_exists(path: Path) -> bool:
    """
    Check if file exists
    Args:
        path (Path): File path
    Returns:
        bool: Whether it exists
    """
    return path.exists() and path.is_file()

def extract_numbers(text: str) -> List[str]:
    """
    Extract all numbers (integers and decimals) from text
    Args:
        text (str): Input text
    Returns:
        List[str]: List of matched number strings
    """
    return re.findall(r'\b\d+\.?\d*\b', text)

def extract_emission_factors(text: str, fuel_name: str) -> Tuple[str, str, str, str]:
    """
    Extract emission factors from text (can be adjusted based on actual requirements)
    Args:
        text (str): Input text
        fuel_name (str): Fuel name
    Returns:
        Tuple[str, str, str, str]: (default, unit, lower, upper)
    """
    default_pattern = rf'{fuel_name}.*?Default:?\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    lower_pattern = rf'{fuel_name}.*?Lower:?\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    upper_pattern = rf'{fuel_name}.*?Upper:?\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    default_match = re.search(default_pattern, text, re.IGNORECASE)
    lower_match = re.search(lower_pattern, text, re.IGNORECASE)
    upper_match = re.search(upper_pattern, text, re.IGNORECASE)
    if default_match and lower_match and upper_match:
        return (
            default_match.group(1),
            default_match.group(2),
            lower_match.group(1),
            upper_match.group(1)
        )
    return ("[Unable to extract default value]", "[Unable to extract unit]", "[Unable to extract lower limit]", "[Unable to extract upper limit]")

def log_error(msg: str, exc: Exception = None):
    """
    Unified error log output
    Args:
        msg (str): Error message
        exc (Exception, optional): Exception object
    """
    print(f"[ERROR] {msg}")
    if exc:
        print(f"Exception: {exc}")

async def run_with_semaphore(tasks: List[Any], max_concurrent: int = 3) -> List[Any]:
    """
    Use semaphore to control concurrent execution of a group of async tasks
    Args:
        tasks (List[Any]): List of coroutine tasks
        max_concurrent (int): Maximum concurrency
    Returns:
        List[Any]: List of task results
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(t) for t in tasks))

def extract_coal_gas_values(text: str, fuel_name: str):
    """
    Try to extract default values, units, and upper/lower limits of coal/natural gas emission factors from text lists or Markdown tables
    Args:
        text (str): Input text
        fuel_name (str): Fuel name
    Returns:
        Tuple[str, str, str, str]: (default, unit, lower, upper)
    """
    import re
    # Strategy 1: Pure text list
    default_pattern_text = r'CO₂ Default:\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    lower_pattern_text = r'CO₂ Lower:\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    upper_pattern_text = r'CO₂ Upper:\s*([0-9,.]+)\s*(kg\/TJ|kgCO2\/TJ|t\/TJ|tCO2\/TJ)'
    default_match_text = re.search(default_pattern_text, text, re.IGNORECASE)
    lower_match_text = re.search(lower_pattern_text, text, re.IGNORECASE)
    upper_match_text = re.search(upper_pattern_text, text, re.IGNORECASE)
    if default_match_text and lower_match_text and upper_match_text:
        default = default_match_text.group(1).replace(',', '')
        lower = lower_match_text.group(1).replace(',', '')
        upper = upper_match_text.group(1).replace(',', '')
        unit = default_match_text.group(2).replace(' ', '')
        return default, unit, lower, upper
    # Strategy 2: Markdown table
    table_pattern = rf"^{re.escape(fuel_name)}\s+([0-9,.]+)\s+([0-9,.]+)\s+([0-9,.]+)"
    table_match = re.search(table_pattern, text, re.MULTILINE | re.IGNORECASE)
    if table_match:
        default = table_match.group(1).replace(',', '')
        lower = table_match.group(2).replace(',', '')
        upper = table_match.group(3).replace(',', '')
        unit = "kgCO2/TJ"
        return default, unit, lower, upper
    return "[Unable to extract default value]", "[Unable to extract unit]", "[Unable to extract lower limit]", "[Unable to extract upper limit]"

def get_formatted_coal_gas_factors(fuel_name: str, response: dict) -> str:
    """
    Format coal and natural gas emission factor results
    Args:
        fuel_name (str): Fuel name
        response (dict): LLM response result
    Returns:
        str: Formatted string
    """
    default, unit, lower, upper = extract_coal_gas_values(response["result"], fuel_name)
    return f"{fuel_name}: {default} {unit} ({lower}, {upper})"

def process_biomass_response(response: dict) -> str:
    """
    Process biomass emission factor response, return formatted string
    Args:
        response (dict): LLM response result
    Returns:
        str: Formatted string
    """
    import re
    import numpy as np
    response_txt = response["result"]
    numbers = re.findall(r'\b\d+\.?\d*\b', response_txt)
    if numbers:
        values = [float(num) for num in numbers]
        if len(values) <= 2:
            return "Biomass: Insufficient number of values (cannot calculate)"
        filtered_values = sorted(values)[1:-1]
        avg = np.mean(filtered_values)
        units = "kg CO₂/MWh"
        return f"Biomass: {avg:.2f} {units} ({min(values):.2f}-{max(values):.2f})"
    else:
        return "Biomass: No values extracted (cannot calculate)"

def format_emission_response(response: dict) -> str:
    """
    Generic response formatting (like print_response in power_emission.py)
    Args:
        response (dict): LLM response result
    Returns:
        str: Formatted string
    """
    import re
    response_txt = response["result"]
    coal_value = None
    gas_value = None
    biomass_value = None
    unit = "g CO₂/kWh"
    # Match average values in table rows
    coal_table_pattern = re.compile(r'(?:hard coal|coal).*?(\d+)\s*[|]?$', re.IGNORECASE | re.MULTILINE)
    gas_table_pattern = re.compile(r'(?:natural gas).*?(\d+)\s*[|]?$', re.IGNORECASE | re.MULTILINE)
    biomass_table_pattern = re.compile(r'(?:biomass).*?(\d+)\s*[|]?$', re.IGNORECASE | re.MULTILINE)
    # Match units
    unit_match = re.search(r'(g\s*CO₂(?:eq)?/kWh|g\s*CO2(?:eq)?/kWh)', response_txt)
    if unit_match:
        unit = unit_match.group(1).replace("CO2", "CO₂").replace(" ", "")
    # Extract coal, gas, biomass
    coal_match = coal_table_pattern.search(response_txt)
    if coal_match:
        coal_value = coal_match.group(1)
    gas_match = gas_table_pattern.search(response_txt)
    if gas_match:
        gas_value = gas_match.group(1)
    biomass_match = biomass_table_pattern.search(response_txt)
    if biomass_match:
        biomass_value = biomass_match.group(1)
    result_text = ""
    if coal_value:
        result_text += f"Coal: {coal_value}{unit}\n"
    if gas_value:
        result_text += f"Natural gas: {gas_value}{unit}\n"
        if not biomass_value:
            biomass_value = gas_value
    if gas_value:
        result_text += f"Biomass: {gas_value}{unit}\n"
    elif biomass_value:
        result_text += f"Biomass: {biomass_value}{unit}\n"
    if not result_text:
        result_text = "Unable to extract average data from response. Please check response format or modify extraction logic.\n"
    return result_text
