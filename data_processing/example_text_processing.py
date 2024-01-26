

def get_text_between_parentheses(text):
    match = re.search(r'\((.*?)\)', text)
    if match:
        return match.group(1)
    return None