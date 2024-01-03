import os
import json
from bs4 import BeautifulSoup

# Folder containing your HTML files
folder_path = '../data_files/_original_files/html/'

# Function to parse an HTML file and extract profile info
def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        profile_info = soup.find('div', class_='profile-info')
        if profile_info:
            name_label = profile_info.find(string='Name:')
            phone_label = profile_info.find(string='Phone Number:')
            email_label = profile_info.find(string='Email:')

            name = name_label.next_element.strip() if name_label else 'N/A'
            phone_number = phone_label.next_element.strip() if phone_label else 'N/A'
            email = email_label.next_element.strip() if email_label else 'N/A'

            return {
                'Name': name,
                'Phone Number': phone_number,
                'Email': email
            }

# List to hold all profiles
all_profiles = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        profile = parse_html(file_path)
        if profile:
            all_profiles.append(profile)

# Convert to JSON
json_data = json.dumps(all_profiles, indent=4)
print(json_data)

# Optionally, save to a JSON file
with open('profiles.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)