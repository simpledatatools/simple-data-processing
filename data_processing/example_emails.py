import mailbox
import json
from email.utils import parsedate_to_datetime

# Replace with your mbox file path
mbox_path = 'path/to/your/mbox/file.mbox'

# Open the mbox file
mbox = mailbox.mbox(mbox_path)

# List to hold email data
emails = []

# Loop through messages in the mbox
for message in mbox:
    email_data = {}

    # Extract email subject
    email_data['subject'] = message['subject']

    # Extract email sender
    email_data['from'] = message['from']

    # Extract the date and convert to a readable format
    date = message['date']
    if date:
        parsed_date = parsedate_to_datetime(date)
        email_data['date'] = parsed_date.isoformat()

    # Extract email body
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = part.get("Content-Disposition")
            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                email_data['body'] = part.get_payload(decode=True).decode()
                break
    else:
        email_data['body'] = message.get_payload(decode=True).decode()

    emails.append(email_data)

# Convert list to JSON
json_emails = json.dumps(emails, indent=4)

# Print JSON string (or you can write it to a file)
print(json_emails)



# Unknown file structure

def process_mbox_file(file_path, emails_list):
    # Open the mbox file
    mbox = mailbox.mbox(file_path)

    # Loop through messages in the mbox
    for message in mbox:
        email_data = {'file_name': os.path.basename(file_path)}

        # Extract email subject, sender, date, and body
        email_data['subject'] = message['subject']
        email_data['from'] = message['from']
        date = message['date']
        if date:
            parsed_date = parsedate_to_datetime(date)
            email_data['date'] = parsed_date.isoformat()
        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
                content_disposition = part.get("Content-Disposition")
                if content_type in ['text/plain', 'text/html'] and 'attachment' not in content_disposition:
                    email_data['body'] = part.get_payload(decode=True).decode()
                    email_data['body_type'] = content_type
                    break
        else:
            email_data['body'] = message.get_payload(decode=True).decode()
            email_data['body_type'] = message.get_content_type()

        emails_list.append(email_data)

def explore_directory(directory, emails_list):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            # If it's a directory, explore it recursively
            explore_directory(path, emails_list)
        elif item.endswith('.mbox'):
            # If it's an mbox file, process it
            process_mbox_file(path, emails_list)

# Replace with your top-level directory path
top_level_directory = 'path/to/your/top-level/directory'

# List to hold all emails from all mbox files
all_emails = []

# Start exploring from the top-level directory
explore_directory(top_level_directory, all_emails)

# Convert list to JSON
json_emails = json.dumps(all_emails, indent=4)

# Print JSON string (or you can write it to a file)
print(json_emails)