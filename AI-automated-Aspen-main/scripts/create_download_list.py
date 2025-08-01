import os
from locations import DATA_DIR

# get all "full_file_list_*.txt" files in the data directory
file_list_files = [f for f in os.listdir(DATA_DIR) 
                   if f.startswith("full_file_list_") 
                   and f.endswith(".txt")]

# Create output file path
output_file = os.path.join(DATA_DIR, "all_download_links.txt")

# Process all files and write to a single output file
all_links = []
for file in file_list_files:
    with open(os.path.join(DATA_DIR, file), "r") as f:
        links = f.read().strip().split("\n")
        # Convert GitHub URLs to raw format and filter for .bkp or .BKP files
        links = [link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/") 
                for link in links if link.strip() and (link.lower().endswith('.bkp'))]
        all_links.extend(links)

# Write all unique links to the output file
with open(output_file, "w") as f:
    f.write("\n".join(set(all_links)))

print(f"Created {output_file} with {len(set(all_links))} unique download links")



