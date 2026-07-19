import re

# Email Validation
def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(email_pattern, email):
        return True
    else:
         print("Invalid email address")
         return False

# Password Validation
def validate_password(password):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

    if re.fullmatch(password_regex, password):
        return True
    else:
        print("Incorrect password format")
        return False

# Stored User Information
user_info = {
    "name": "Karthik",
    "email": "karthik@datavalley.ai",
    "password": "Karthik123"
}

# User Input
email = input("Enter your email address: ")
password = input("Enter the password: ")

# Validation
if validate_email(email) and validate_password(password):

    if user_info["email"] == email and user_info["password"] == password:
        print("Credentials are valid")
    else:
        print("Incorrect credentials")