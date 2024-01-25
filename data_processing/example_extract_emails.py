import re

def extract_emails(text):
    # Regular expression pattern for matching emails
    # This pattern accounts for optional angle brackets around the email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    bracketed_email_pattern = r'<(' + email_pattern + r')>'
    
    # Find all bracketed emails and remove brackets
    bracketed_emails = re.findall(bracketed_email_pattern, text)
    
    # Find all regular emails
    emails = re.findall(email_pattern, text)

    # Combine and remove duplicates
    all_emails = list(set(emails + bracketed_emails))

    return all_emails

# Example usage
text = "Example emails: test@example.com, <another.email123@example.co.uk>, email@test-domain.com, <email-with-brackets@example.com>"
extracted_emails = extract_emails(text)
print(extracted_emails)