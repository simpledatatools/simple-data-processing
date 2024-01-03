import os
import zipfile
import shutil
from bs4 import BeautifulSoup

# Specify the folder containing the ZIP files
folder_path = '../data_files/_original_files/zips/'

def process_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        # Additional processing can be done here
        # print(soup)
        print(f"Processed {file_path}")

def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Filter out unwanted macOS-specific files and directories
        for member in zip_ref.namelist():
            # Create a valid path by removing the filename and keeping the directory structure
            directory = os.path.join(extract_path, os.path.dirname(member))

            # Skip macOS specific files
            if '__MACOSX' in directory or member.endswith('.DS_Store'):
                continue

            # Create the directory if it does not exist
            if not os.path.exists(directory):
                os.makedirs(directory)

            # If the member is not a directory, extract the file
            if not member.endswith('/'):
                source = zip_ref.open(member)
                target_file_path = os.path.join(extract_path, member)
                with source, open(target_file_path, "wb") as target:
                    target.write(source.read())

def find_first_directory(path):
    """Finds and returns the first directory in the given path."""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            return item_path
    return None

# Iterate through each file in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith('.zip'):
        zip_path = os.path.join(folder_path, filename)
        print(f"Processing ZIP file: {filename}")

        temp_extract_path = os.path.join(folder_path, 'temp_' + filename[:-4])  # Temporary extraction path
        extract_zip(zip_path, temp_extract_path)

        # Find the first directory inside the temp extraction path
        actual_extract_path = find_first_directory(temp_extract_path)
        if not actual_extract_path:
            print(f"No directory found in ZIP file: {filename}")
            shutil.rmtree(temp_extract_path)
            continue

        index_html_path = os.path.join(actual_extract_path, 'index.html')
        if os.path.exists(index_html_path):
            process_html(index_html_path)
        else:
            print('Main index.html file is missing')

        messages_folder = os.path.join(actual_extract_path, 'messages')
        if os.path.isdir(messages_folder):
            messages_index_html = os.path.join(messages_folder, 'index.html')
            if os.path.exists(messages_index_html):
                process_html(messages_index_html)
            else:
                print('Messages index.html file is missing')
        else:
            print('Messages folder missing')

        # Delete the temporary unzipped folder after processing
        shutil.rmtree(temp_extract_path)

print("All ZIP files processed.")