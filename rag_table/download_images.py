
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_spec_images(url, save_dir, verbose=True):
    if verbose:
        print(f"--- Precision Download Mode ---")
        print(f"Accessing webpage: {url}")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        if verbose:
            print(f"Failed to request webpage: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Ensure save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        if verbose:
            print(f"Created directory: {save_dir}")

    # Final, correct locating logic: find images where src contains '/Upload/ueditor/'
    spec_images = [img for img in soup.find_all('img') if img.get('src') and '/Upload/ueditor/' in img.get('src')]

    if not spec_images:
        if verbose:
            print("Error: Could not find specification table images (src contains '/Upload/ueditor/').")
        return
        
    if verbose:
        print(f"Located successfully! Found {len(spec_images)} specification table images, preparing to download...")

    image_names = ["gxt_spec_table_part1.jpg", "gxt_spec_table_part2.jpg"]

    for i, img_tag in enumerate(spec_images):
        if i >= len(image_names):
            break

        img_src = img_tag.get('src')
        img_url = urljoin(url, img_src)
        
        try:
            # Get high-quality original images without any compression
            img_response = requests.get(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_response.raise_for_status()
            img_data = img_response.content
            
            file_path = os.path.join(save_dir, image_names[i])
            with open(file_path, 'wb') as handler:
                handler.write(img_data)
            if verbose:
                print(f"Successfully downloaded high-resolution image: {file_path} (Size: {len(img_data)} bytes)")
        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"Failed to download image {img_url}: {e}")

if __name__ == '__main__':
    target_url = "<your base url>"
    output_directory = "web_content"
    download_spec_images(target_url, output_directory)
    print("\nImage download script finished.")