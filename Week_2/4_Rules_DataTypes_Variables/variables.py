email = "support@datavalley.ai"
password = "Test@123"
pin_code = 500001
company_name = "Datavalley"
bank_balance = 52900.56
is_account_active = True

print("Email Address: ",email)
print(pin_code)
print(bank_balance)

print(type(pin_code))
print(type(bank_balance))
print(type(email))
print(type(is_account_active))

message = """Snake case is a naming convention.
It uses lowercase letters.
Words are separated using underscores."""

print(message)

employees = ["Lokesh", "Ganesh", "Charan", "Naveen","Naveen",
    "Naveen",]
print(employees[3])
print(len(employees))
print(employees)
employees.remove("Ganesh")
employees.append("Rakesh")
print(employees)

product_info = {
    "name": "realme NARZO 80 Pro 5G",
    "avg_rating": 4.3,
    "rating_count": 2600,
    "discount": 14,
    "price": 27999
}

print(product_info["name"])
print(product_info["price"])

