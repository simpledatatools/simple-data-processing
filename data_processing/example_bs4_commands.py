# BeautifulSoup Cheat Sheet for HTML Processing
# Import necessary libraries
from bs4 import BeautifulSoup
import re

# Sample HTML (Replace with actual HTML content)
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<a href="http://example.com/one" class="sister" id="link1">One</a>
<a href="http://example.com/two" class="sister" id="link2">Two</a>
<table><tr><td>Row 1, Cell 1</td><td>Row 1, Cell 2</td></tr></table>
</body>
</html>
"""

# Load HTML into BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Finding Elements

# Find First Occurrence of a Tag
first_paragraph = soup.find('p')

# Find All Occurrences of a Tag
all_paragraphs = soup.find_all('p')

# Find Using a Class
elements_with_class = soup.find_all('div', class_='sample-class')

# Find Using an ID
element_with_id = soup.find(id='sample-id')

# Find Tags with Specific Attributes
custom_tags = soup.find_all('tag', {'attribute': 'value'})

# Find Tags by Text Content
tags_with_text = soup.find_all('tag', string='Text')

# Find a Tag within Another Tag
inner_tag = soup.find('outer_tag').find('inner_tag')

# Find Multiple Tags
multiple_tags = soup.find_all(['h1', 'h2', 'h3'])

# Navigating the Tree

# Accessing Parent Elements
parent_element = soup.find('tag').parent

# Accessing Sibling Elements
next_sibling = soup.find('tag').next_sibling
previous_sibling = soup.find('tag').previous_sibling

# Accessing Child Elements
child_elements = soup.find('tag').contents  # or .children for iterator

# Accessing Descendants
all_descendants = soup.find('tag').descendants

# Extracting Information

# Get Text Content from a Tag
text = soup.find('tag').get_text()

# Extracting an Attribute Value from a Tag
attribute_value = soup.find('tag')['attribute']

# Extracting All Links
links = [a['href'] for a in soup.find_all('a', href=True)]

# Extracting a Data Table
rows = soup.find('table').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    # Process 'cols': List of column values

# Extracting All Text from a Page
page_text = soup.get_text()

# Advanced Searching

# Using CSS Selectors
elements = soup.select('div.sample-class p')

# Searching by CSS Class
elements = soup.find_all(class_='sample-class')

# Using Lambda Functions
custom_find = soup.find_all(lambda tag: tag.name == 'tag' and tag.get('attribute') == 'value')

# Finding Using Regular Expressions
tags = soup.find_all(re.compile("^b"))  # Tags that start with 'b'

# Modifying the Tree

# Change an Attribute
soup.find('tag')['attribute'] = 'new value'

# Add a New Attribute
soup.find('tag')['new-attribute'] = 'value'

# Remove an Attribute
del soup.find('tag')['attribute']

# Replace a Tag
soup.find('old_tag').replace_with(soup.new_tag('new_tag'))

# Pretty Printing

# Prettify the HTML
pretty_html = soup.prettify()

# Miscellaneous

# Parsing Only Part of a Document
soup = BeautifulSoup(html_doc, 'html.parser', parse_only=SoupStrainer('tag'))

# Dealing with Non-HTML/XML
comment = soup.find(string=lambda text: isinstance(text, Comment))

# Encoding to UTF-8
encoded_html = soup.encode('utf-8')

# Print out the first paragraph text
print(first_paragraph.get_text())