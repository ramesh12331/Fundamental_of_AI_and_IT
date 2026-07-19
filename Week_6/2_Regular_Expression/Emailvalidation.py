import re

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(email_pattern, email):
        print("Valid email address")
        return True
    else:
         print("Invalid email address")
         return False

email = input("Enter your email address: ")
validate_email(email)