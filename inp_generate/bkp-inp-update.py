import os
import win32com.client
import time
from pathlib import Path
import sys

def process_bkp_file(bkp_path, output_folder):
    """
    Process a single BKP file and export it to INP format
    
    Args:
        bkp_path (str): Full path to the BKP file
        output_folder (str): Output directory path for INP files
    
    Returns:
        bool: True if processing successful, False otherwise
    """
    try:
        print("Step 1: Creating Aspen instance...")
        aspen = win32com.client.Dispatch("Apwn.Document")
        print("Aspen instance created successfully")
        time.sleep(1)  # Wait for instance to fully initialize
        
        # Set output filename
        output_name = Path(bkp_path).stem + ".inp"
        output_path = os.path.join(output_folder, output_name)
        print(f"Step 2: Output file path set to: {output_path}")
        
        print(f"Step 3: Loading file: {bkp_path}")
        aspen.InitFromArchive(str(bkp_path))
        print("File loaded successfully")
        time.sleep(2)  # Give more time for file loading
        
        print("Step 4: Setting Visible property...")
        aspen.Visible = True
        print("Visible property set successfully")
        
        print("Step 5: Setting SuppressDialogs property...")
        aspen.SuppressDialogs = 1
        print("SuppressDialogs property set successfully")
        time.sleep(1)
        
        print("Step 6: Executing Reinit...")
        aspen.Reinit()
        print("Reinit executed successfully")
        time.sleep(1)
        
        print("Step 7: Running simulation...")
        aspen.Engine.Run2()
        print("Simulation completed")
        time.sleep(1)
        
        print("Step 8: Exporting INP file...")
        aspen.Export(4, output_path)
        print("INP file exported successfully")
        
        print(f"All steps completed, file exported to: {output_path}")
        return True
        
    except Exception as e:
        print(f"\nError Details:")
        print(f"- Error Type: {type(e).__name__}")
        print(f"- Error Message: {str(e)}")
        print(f"- Error Location: Current execution step")
        return False
    finally:
        try:
            if 'aspen' in locals():
                print("Closing Aspen instance...")
                aspen.Quit()
                del aspen
                print("Aspen instance closed")
        except:
            print("Issue occurred while closing Aspen instance, but won't affect main program")

def batch_process_bkp_files(input_folder, output_folder):
    """
    Batch process all BKP files in a folder
    
    Args:
        input_folder (str): Input directory containing BKP files
        output_folder (str): Output directory for INP files
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all BKP files
    bkp_files = list(Path(input_folder).glob("*.bkp"))
    total_files = len(bkp_files)
    
    if total_files == 0:
        print("No BKP files found!")
        return
        
    print(f"Found {total_files} BKP files")
    
    # Process each file
    success_count = 0
    for i, bkp_file in enumerate(bkp_files, 1):
        print(f"\n{'='*50}")
        print(f"Processing file {i}/{total_files}: {bkp_file.name}")
        print(f"{'='*50}")
        
        if process_bkp_file(bkp_file, output_folder):
            success_count += 1
            print(f"\nFile processed successfully: {bkp_file.name}")
        else:
            print(f"\nFile processing failed: {bkp_file.name}")
            
        print(f"{'='*50}\n")
        # Pause briefly after each file
        time.sleep(3)
    
    # Print summary
    print(f"\nProcessing complete! Successfully converted {success_count}/{total_files} files")

if __name__ == "__main__":
    # Set relative input and output folder paths
    input_folder = "bkp_all"
    output_folder = "inp_outputs"
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder {input_folder} does not exist!")
        sys.exit(1)
    
    # Start processing
    print(f"\nStarting batch BKP file processing...")
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}")
    
    try:
        batch_process_bkp_files(input_folder, output_folder)
    except Exception as e:
        print(f"Program execution error: {str(e)}")
        sys.exit(1)