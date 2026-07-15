# JSON - Javascript Object Notation - It is a light weight data interchangable format that is easy to read and write.
# import json

# json.dumps() - Converts Python object into JSON string - Sending information to external source.
# json.loads() - Converts JSON string into Python object - Receiving information from external source

import json

product_info = {
    "product_id": "PRD004",
    "name": "Dell UltraSharp 27",
    "brand": "Dell",
    "price": 599.99,
    "discount": 5,
    "quantity": 1,
    "rating": 4.7,
}

json_str = json.dumps(product_info)
print(json_str)
# Output:
# {"product_id": "PRD004", "name": "Dell UltraSharp 27", "brand": "Dell", "price": 599.99, "discount": 5, "quantity": 1, "rating": 4.7}

print(json_str[0:5])
# Output:
# {"pro

product_info = json.loads(json_str)

print(product_info['product_id'])
# Output:
# PRD004

# ==============================================================

# ==============================================================
# WEB SCRAPING
# ==============================================================


import requests

# =====================================================
#   BASIC CONNECTION
# =====================================================

url = "https://www.shine.com/job-search/python-developer-jobs?suid=492ef81f-b981-478f-a326-43ab2ccfd32c&q=python-developer&qActual=Python+developer&minexp=2&hidden_id_exp=2"

headers = {
    "User-Agent"      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept"          : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-US,en;q=0.5",
}

# =====================================================
#   GET REQUEST
# =====================================================

response = requests.get(url, headers=headers, timeout=10)

html_content = response.text

print(html_content)
# Output:
# Prints the raw HTML source of the Shine.com job search results page
# (the full <html> markup returned by the server for the given URL).