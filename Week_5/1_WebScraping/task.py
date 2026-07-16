import requests
from bs4 import BeautifulSoup

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
# print(html_content)   # raw HTML of the job search page (only needed for debugging selectors)

# =====================================================
#   PARSE WITH BEAUTIFULSOUP
# =====================================================
soup = BeautifulSoup(html_content, 'html.parser')

product_card = soup.find_all("a", class_="_3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _1i2djtb9 _1i2djt29 _1i2djt4i _1i2djtef _1i2djtgc _1i2djtko _1i2djtif")
# print(product_card)

# =====================================================
#   EXTRACT FIELDS FROM EACH JOB CARD
# =====================================================
products = []

for product in product_card:
    print("-"*20)
    # product_image = product.find("div", class_="_3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _1i2djtb9 _1i2djt0 _9nihix56")
    # print(product_image.text)
    product_name = product.find("div", class_="_3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzqk _1i2djtb9 _1i2djt0 _1i2djti9")
    # print(product_name.text)
    product_title = product.find("div", class_="_58bkzq6c _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzq2 _1i2djtb9 _1i2djt0 _1i2djtk9")
    # print(product_title.text)
    product_discount = product.find("div", class_="_58bkzq6z _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzqo _1i2djtb9 _1i2djt0 _1i2djti9")
    # print(product_discount.text)
    product_fixed_price = product.find("div", class_="_58bkzq6c _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzqp _1i2djtb9 _1i2djt0 _1i2djti9")
    # print(product_fixed_price.text)
    product_vary_price = product.find("div", class_="_3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzqo _1i2djtb9 _1i2djt0 _1i2djtk9")
    # print(product_vary_price.text)
    product_upi_price = product.find("div", class_="_58bkzq5q _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzql _1i2djtb9 _1i2djt0 _1i2djti3")
    # print(product_upi_price.text)
    product_upi_off = product.find("div", class_="_58bkzq5q _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzq2 _1i2djtb9 _1i2djt0")
    # print(product_upi_off.text)

    products.append({
        "product_name" : product_name.text,
        "product_title" : product_title.text,
        "product_discount" : product_discount.text,
        "product_fixed_price" : product_fixed_price.text,
        "product_vary_price" : product_vary_price.text,
        "product_upi_price" : product_upi_price.text,
        "product_upi_off" : product_upi_off.text
    })
print(products)

import json

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)