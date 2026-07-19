import re 

def validate_password(password):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

    if re.fullmatch(password_regex, password):
        print("Valid password format")
        return True
    else:
        print("Incorrect password format")
        return False

password = input("Enter the password: ")
validate_password(password)