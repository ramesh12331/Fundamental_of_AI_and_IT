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
print(product_info["product_id"])