mobiles = [
    {
        "name": "realme NARZO 80 Pro 5G (Speed Silver, 8GB+256GB)",
        "avg_rating": 4.6,
        "rating_count": 2600,
        "price": 25999,
        "discount": 14,
        "colors": [
            "Hyper Black",
            "Vivid Mint"
        ],
        "reviews": [
            {
                "name": "Sandeep Kumar",
                "rating": 2.0,
                "title": "Heating problem",
                "description": "Heating issue with this phone not recommended."
            },
            {
                "name": "Manjesh",
                "rating": 4.0,
                "title": "Awesome mobile",
                "description": "Recommended mobile."
            }
        ]
    },
    {
        "name": "iQOO Z10R 5G (Moonstone, 12GB RAM, 256GB Storage)",
        "avg_rating": 4.4,
        "rating_count": 4300,
        "price": 26999,
        "discount": 0,
        "reviews": []
    },
    {
        "name": "OnePlus Nord CE6 Lite",
        "avg_rating": 4.2,
        "rating_count": 20,
        "price": 31999,
        "discount": 28,
        "reviews": []
    }
]

# Discount of second mobile
print(mobiles[1]["discount"])

# Rating of second review of first mobile
print(mobiles[0]["reviews"][1]["rating"])

# Second color of first mobile
print(mobiles[0]["colors"][1])

# First review title
print(mobiles[0]["reviews"][0]["title"])

# First review description
print(mobiles[0]["reviews"][0]["description"])

# Second review description
print(mobiles[0]["reviews"][1]["description"])

# =============================================

# Task: Create a customers list that includes multiple addresses for each customer.

customers = [
    {
        "name": "Ramesh",
        "mobile": "9876543210",
        "email": "ramesh@gmail.com",
        "addresses": [
            {
                "type": "Home",
                "door_no": "10-2-15",
                "street": "MG Road",
                "city": "Hyderabad",
                "state": "Telangana",
                "pincode": "500001"
            },
            {
                "type": "Office",
                "door_no": "5-12-101",
                "street": "Hitech City",
                "city": "Hyderabad",
                "state": "Telangana",
                "pincode": "500081"
            }
        ]
    },

    {
        "name": "Suresh",
        "mobile": "9123456780",
        "email": "suresh@gmail.com",
        "addresses": [
            {
                "type": "Home",
                "door_no": "2-45",
                "street": "Beach Road",
                "city": "Visakhapatnam",
                "state": "Andhra Pradesh",
                "pincode": "530001"
            },
            {
                "type": "Office",
                "door_no": "11-8-75",
                "street": "Dwaraka Nagar",
                "city": "Visakhapatnam",
                "state": "Andhra Pradesh",
                "pincode": "530016"
            }
        ]
    },

    {
        "name": "Lakshmi",
        "mobile": "9012345678",
        "email": "lakshmi@gmail.com",
        "addresses": [
            {
                "type": "Home",
                "door_no": "3-22",
                "street": "Temple Road",
                "city": "Vijayawada",
                "state": "Andhra Pradesh",
                "pincode": "520001"
            },
            {
                "type": "Office",
                "door_no": "7-45",
                "street": "Benz Circle",
                "city": "Vijayawada",
                "state": "Andhra Pradesh",
                "pincode": "520010"
            }
        ]
    }
]

# Print complete customers list
print(customers)

# First customer name
print(customers[0]["name"])

# First customer's mobile
print(customers[0]['mobile'])

# First customer's first address
print(customers[0]["addresses"][0])

# First customer's home city
print(customers[0]["addresses"][0]["city"])

# First customer's office street
print(customers[0]["addresses"][1]["street"])

# Second customer's office pincode
print(customers[1]["addresses"][1]["pincode"])

# Third customer's home state
print(customers[2]["addresses"][0]["state"])

# Loop through all customers
for customer in customers:
    print(customer["name"])

# Loop through each customer's addresses
for customer in customers:
    print(customer["name"])

    for address in customer["addresses"]:
        print(address["type"], "-", address["city"])
