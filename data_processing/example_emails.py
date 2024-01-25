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