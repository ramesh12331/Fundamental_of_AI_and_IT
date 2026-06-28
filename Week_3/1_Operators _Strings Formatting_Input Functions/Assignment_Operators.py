# 1. Addition Assignment (+=)
balance = 1950
deposit = 500

# balance = balance + deposit
balance += deposit
print(balance)

# 2. Subtraction Assignment (-=)
withdraw = 200
balance -= withdraw
print(balance)

# 3. Multiplication Assignment (*=)
salary = 50000
# salary = salary*1.25
salary *= 1.25
print(salary)

# 4. Division Assignment (/=)
total_bill = 8000
total_bill /= 4
print(total_bill)

# 5. Modulus Assignment (%=)
number = 17
number %= 5
print(number)

# 6. Exponent Assignment (**=)
number = 5
number **= 2
print(number)

# ##Identity Operators##
# is
# Example 1
category1 = "Electronics"
category2 = "Electronics"

print(category1 is category2)

# Example 2
category1 = "Electronics"
category2 = "Clothes"

print(category1 is category2)

# is not

category1 = "Electronics"
category2 = "Clothes"

print(category1 is not category2)

# ##Membership Operators##
# in
# Example 1
product_categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Sports & Fitness",
    "Beauty & Personal Care",
    "Toys & Games"
]

searched_category = "Electronics"
print(searched_category in product_categories)

# Example 2
product_categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Sports & Fitness",
    "Beauty & Personal Care",
    "Toys & Games"
]

searched_category = "Automotive"
print(searched_category in product_categories)

# not in
product_categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Sports & Fitness",
    "Beauty & Personal Care",
    "Toys & Games"
]

searched_category = "Automotive"
print(searched_category not in product_categories)
