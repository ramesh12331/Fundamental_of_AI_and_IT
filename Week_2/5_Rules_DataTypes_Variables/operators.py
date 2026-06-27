# 1. String Concatenation
first_name = "Mamidi"
last_name = "Ramesh"

print(first_name + " " + last_name)

# 2. Address Dictionary
address = {
    "house_no": "12-45",
    "street": "MG Road",
    "area": "Sarojini Devi",
    "city": "Hyderabad",
    "state": "Andhra Pradesh",
    "country": "India",
    "pincode": "500001"
}

print(address["house_no"] + ", " + address["street"] + ", " + address["area"] + ", " + address["city"] + ", " 
+ address["state"] + address["country"] + ", " + address["pincode"] + ".")

# 3. Integer + String Error
num1 = 506
num2 = "405"

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(num1 + num2)

# 4. String Concatenation
num1 = "506"
num2 = "405"

print(num1 + num2)

# 5. Division (/)
total_bill = 1250
friends = 3

bill_per_person = total_bill/friends

print(bill_per_person)

# 6. Floor Division (//)
total_bill = 1250
friends = 3

bill_per_person = total_bill//friends

print(bill_per_person)

# 7. Power Operator (**)
print("Power: ",1200 ** 2)

# ##Comparison Operator##

# 8. Equality Operator (==)
# Example 1
registered_email = 'ganesh@datavalley.ai'
entered_email = 'Ganesh@datavalley.ai'

is_email_matching = registered_email == entered_email
print(is_email_matching) 
# Python is case-sensitive.

# Example 2
registered_email = 'ganesh@datavalley.ai'
entered_email = 'ganesh@datavalley.ai'

is_email_matching = registered_email == entered_email
print(is_email_matching) 

# Example 3
registered_email = 'ganesh@datavalley.ai'
entered_email = 'varun@datavalley.ai'

is_email_matching = registered_email == entered_email
print(is_email_matching) 

# 9. Not Equal (!=)
registered_email = 'ganesh@datavalley.ai'
entered_email = 'ganesh@datavalley.ai'

is_email_matching = registered_email != entered_email
print(is_email_matching) 

# PAN Example
registered_pan = 'ABCD1234E'
entered_pan = 'ABCD1234G'

is_pan_matching = registered_pan != entered_pan
print(is_pan_matching)

# 10. Logical AND
registered_mobile = 9032345245
entered_mobile = 9032345245

registered_password = 'Test@!23'
entered_password = 'Test@!23'

is_mobile_matching = registered_mobile == entered_mobile
is_password_matching = registered_password == entered_password

resultant = is_mobile_matching and is_password_matching
print(resultant)

# Password Changed
registered_pan = 'ABCD1234E'
entered_pan = 'ABCD1234G'

is_pan_matching = registered_pan != entered_pan
print(is_pan_matching)

# 10. Logical AND
registered_mobile = 9032345245
entered_mobile = 9032345245

registered_password = 'Test@!23'
entered_password = 'Hyderabad@!23'

is_mobile_matching = registered_mobile == entered_mobile
is_password_matching = registered_password == entered_password

resultant = is_mobile_matching and is_password_matching
print(resultant)

# 11. Logical OR (One Condition True)
registered_mobile = 9032345245
entered_mobile = 9032345245

registered_email = 'ganesh@datavalley.ai'
entered_email = 'ganesh@datavalley.ai'

resultant = (registered_mobile == entered_mobile) or (registered_password == entered_password)
print(resultant)

# Both Conditions False
registered_mobile = 9032345245
entered_mobile = 9032345248

registered_email = 'ganesh@datavalley.ai'
entered_email = 'varun@datavalley.ai'

resultant = (registered_mobile == entered_mobile) or (registered_password == entered_password)
print(resultant)

# 12. NOT Operator
is_account_suspended = True

is_account_suspended = not is_account_suspended
print(is_account_suspended)





