import os
import subprocess
import time
from datetime import datetime

def run_script(script_name, description):
    """Run a Python script and handle its execution"""
    print(f"\n{'='*50}")
    print(f"Running {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(['python', script_name], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              check=True)
        if result.returncode == 0:
            print(f"\n✓ {description} completed successfully")
            return True
        else:
            print(f"\n× {description} failed with return code {result.returncode}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"\n× {description} failed with error: {e}")
        return False
    except Exception as e:
        print(f"\n× Unexpected error running {description}: {e}")
        return False

def check_generated_report():
    """Check if the RadFrac report file was generated successfully"""
    current_date = datetime.now().strftime("%b %d").lower()
    report_path = os.path.join("inp_generate/simple", f"{current_date}radsimple-general.rep")
    
    print(f"\nChecking generated report file: {report_path}")
    if os.path.exists(report_path):
        print("✓ RadFrac report file found")
        return True
    else:
        print("× RadFrac report file not found")
        return False

def main():
    # Define the scripts to run in order
    scripts = [
        ("bkp-inp-update.py", "Step 1: Convert BKP files to INP format"),
        ("traditional_distillation_inp.py", "Step 2: Generate DSTWU and RadFrac models"),
        ("optimized_condition.py", "Step 3: Apply optimal parameters to simulation"),
        ("traditional_carbon_accounting.py", "Step 4: Calculate carbon emissions"),
        ("image_rr.py", "Step 5: Generate reflux ratio sensitivity analysis chart"),
        ("image_duty.py", "Step 6: Generate reboiler heat duty sensitivity analysis chart"),
        ("heatpump_distillation_inp.py", "Step 7: Generate heat pump distillation model"),
        ("heatpump_carbon_accounting.py", "Step 8: Calculate heat pump carbon emissions"),
        ("image_carbon_emissions.py", "Step 9: Generate carbon emissions comparison chart")
    ]
    
    print("\nStarting sequential execution of all scripts...")
    
    # Run first script to convert BKP files
    success = run_script(scripts[0][0], scripts[0][1])
    if not success:
        print("\nExecution stopped due to failure in BKP to INP conversion")
        return
    
    # Run second script to generate models and report
    success = run_script(scripts[1][0], scripts[1][1])
    if not success:
        print("\nExecution stopped due to failure in model generation")
        return
        
    # Check if the RadFrac report was generated successfully
    if not check_generated_report():
        print("\nExecution stopped due to failure in report generation")
        return
    
    # Run remaining scripts
    for script_name, description in scripts[2:]:
        success = run_script(script_name, description)
        if not success:
            print(f"\nExecution stopped due to failure in {description}")
            break
        time.sleep(2)  # Add delay between steps
    
    print("\nScript execution sequence completed.")
    print("\nGenerated files:")
    print("- Converted INP files from BKP files")
    print("- Aspen Plus simulation models and reports")
    print("- Carbon emission calculations")
    print("- Reflux ratio sensitivity analysis chart (HTML)")
    print("- Reboiler heat duty sensitivity analysis chart (HTML)")
    print("- Heat pump distillation model and report")
    print("- Heat pump carbon emission analysis (Word document)")
    print("- Carbon emissions comparison chart (HTML with export functionality)")

if __name__ == "__main__":
    main() 