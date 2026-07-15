import requests

# =====================================================
#   BASIC CONNECTION
# =====================================================

url = "https://www.flipkart.com/infinite-m3-at-store?param=38437439&BU=Mixed"

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