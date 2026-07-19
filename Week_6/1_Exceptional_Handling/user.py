# ============================================================
# User Defined Exception Example
# InvalidPasswordError
# User Defined Exception with finally Block
# ============================================================
class InvalidPasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)

def login(password):
    correct_password = "Secure@123"

    if password != correct_password:
        raise InvalidPasswordError("Invalid password entered!")
    else:
        print("Login successful!")

try:
    password = input("Enter your password: ")
    login(password)
except InvalidPasswordError as e:
    print(e)
finally:
    print("Login process completed.")