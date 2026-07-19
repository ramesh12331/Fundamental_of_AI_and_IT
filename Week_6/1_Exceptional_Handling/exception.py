# 1.Example (Without Exception Handling)
loan_amount = float(input("Enter the loan amount: "))
months = int(input("Enter the repayment months: "))

emi = loan_amount/months
print(f'EMI: {emi}')

# ============================================================
# Python Exception Handling 
# ============================================================

# 1) ZeroDivisionError Example
# A user accidentally enters 0 months for the EMI calculation,
# causing a ZeroDivisionError

try:
    loan_amount = float(input("Enter the loan amount: "))
    months = int(input("Enter the repayment months: "))

    emi = loan_amount/months
    print(f'EMI: {emi}')
except ZeroDivisionError:
    print("Repayment months cannot be zero!")
except ValueError:
    print("Invalid input! Please enter only numbers.")

# 2) KeyError Example
# Accessing a dictionary key that does not exist

employee = {
    "name": "Karthik"
}

try:
    print(employee["id"])

except KeyError:
    print("Key not found in dictionary!")

# ============================================================
# 3) Coupon Code Example with KeyError Handling
coupons = {
    "SAVE10": 10,
    "SAVE20": 20,
    "WELCOME50": 50,
    "HOTEL15": 15,
    "SUMMER30": 30
}

try:
    coupon_code = input("Enter your coupon code: ").strip(" ").upper()
    discount = coupons[coupon_code]
    print(f"Coupon applied! you got {discount}% off")
except KeyError:
    print("Invalid coupon code!")

# ============================================================

# 4) List IndexError Example
# Selecting a player using an invalid index
# Finally Block Example
is_loading = True
print("Page is loading...")

try:
    players = [
        "Virat Kohli",
        "Rohit Sharma",
        "MS Dhoni",
        "Jasprit Bumrah",
        "Ravindra Jadeja",
        "Steve Smith",
        "Pat Cummins",
        "Joe Root",
        "Ben Stokes",
        "Babar Azam"
    ]

    print(len(players))
    player_no = int(input("Select player (0-9): "))
    is_loading = False
    print(f"Selected player: {players[player_no]}")

except IndexError:
    print("Select the player only between 0 & 9")
    is_loading = False
    print("Stopped loading the page!")
except ValueError:
    print("Invalid input! Please enter a number.")
    is_loading = False
    print("Stopped loading the page!")
finally:
    is_loading = False
    print("Stopped loading the page!")

# ============================================================

# 5) Custom Exception-like Example
# Database connection and failure message

class Database:
    def connect(self):
         print("Connected to database")
    def close(self):
        print("Disconnected from database")

try:
    db = Database()
    db.connect()
    raise Exception("Database query failed!")
except Exception as e:
    print(e)
finally:
    db.close()