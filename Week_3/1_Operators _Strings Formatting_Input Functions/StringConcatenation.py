# String Concatenation
# Example - Full Name

firstname = input("Enter the first name: ")
lastname = input("Enter the last name: ")
fullname = firstname + " " + lastname
print(fullname)

# Example - Creating an Address

address = {
    "house_no": "12-45/A",
    "street": "MG Road",
    "area": "Banjara Hills",
    "city": "Hyderabad",
    "state": "Telangana"
}

address_str = (address["house_no"] + ", " + address["street"] + ", " + address["area"] + ", " + address["city"] + ", " + address["state"] + ".")
print(address_str)

# Formatted String (f-string)
address_str = f"{address["house_no"]}, {address["street"]}, {address["area"]}, {address["city"]}, {address["state"]}"
print(address_str)

# Example - Email Template using f-string
student_name = "Karthik"
date = "24/05/2026"
sender_name = "Data Valley"

email_template = f"""
Dear {student_name},

This is a reminder that the AI class is scheduled on {date} at 8:00 AM.

Please join the session on time and be prepared with your laptop and required materials.

Thank you.

Best Regards,
{sender_name}
"""
print(email_template)