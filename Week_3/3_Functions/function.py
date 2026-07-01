#### Function to Calculate Sum ####
# Function Definition

def calculate_sum(a,b):
    sum = a + b
    print("Sum: ",sum)

# Function Calls
calculate_sum(35,45)
calculate_sum(12, 15)
calculate_sum(45, 90)

# ============================================
# Greeting Function
def greet():
    print("Good Morning Folks")

greet()
greet()
greet()

# ============================================
# Product using Return Statement
def calculate_product(a,b):
    product = a*b
    return product
result = calculate_product(4,5)
print(result)

# ============================================
# Construct Full Name
def construct_fullname(firstname, middlename, lastname):
    fullname = f"{firstname} {middlename} {lastname}".upper()
    print("Full Name: ",fullname)

construct_fullname("Aravelli", "Uday", "Kiran")
construct_fullname("Mamidi", "" ,"Ramesh")

# ============================================
# Mini Project 1: Banking System
def check_balance(balance):
    print(f"Your current balance is {balance}")

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal is successfull, new balance is {balance}")
        return balance

# Checking Balance
account_balance = 5000
check_balance(account_balance)

# Withdraw Example 1
# withdraw(account_balance, 2000)
# withdraw(account_balance, 4050)

# Updating Balance After Every Withdrawal
account_balance = withdraw(account_balance, 2000)
account_balance = withdraw(account_balance, 200)
account_balance = withdraw(account_balance, 450)

# ============================================
# Mini Project 2: Discount Calculator
def calculate_discounted_amount(total_amount):
    
    if total_amount >= 5000:
        discounted_amount = total_amount - (total_amount * 0.20)
        return discounted_amount
    elif total_amount >= 3000:
        discounted_amount = total_amount - (total_amount * 0.10)
        return discounted_amount
    elif total_amount >= 1000:
        discounted_amount = total_amount - (total_amount * 0.05)
        return discounted_amount
    else:
        return total_amount
    
# Example 1
discounted_amount = calculate_discounted_amount(50000)
print(discounted_amount)

# Example 2
discounted_amount = calculate_discounted_amount(4500)
print(discounted_amount)