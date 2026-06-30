# 1. Taking User Input
# age = input("Enter your age: ")

# if age>18:
    # TypeError: '>' not supported between instances of 'str' and 'int'
    # print("You are eligible to vote!")

# Correct Code
age = int(input("Enter your age: "))

if age>18:
    print("You are eligible to vote!")

# 2. Boolean Example
is_account_activated = True

if is_account_activated:
    print("Your account is in active state")
else:
    print("Your account is in deactivated state")

# 3. ATM Withdrawal Example
balance = 4500
amount = float(input("Enter the amount: "))

if balance >= amount:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance is {balance}")
else:
    print("Insufficient balance")

# 4. Login Validation Using Dictionary
user = {
    "name": "Ramesh",
    "email": "ramesh90@gmail.com",
    "password": "Ramesh@24"
}

entered_email = input("Enter email: ")
entered_password = input("Enter password: ")

if entered_email == user["email"] and entered_password == user["password"]:
    print("Credentials are valid")
else:
    print("Incorrect email or password")

# 5. Truthy and Falsy Values
balance = -100

if balance:
    print("Status")

# Example1
if 0:
    print("Hello") #Nothing prints.

# Example2
if -10:
    print("Hello Hi")

# 6. Traffic Signal using if-elif-else
selected_option = input("Enter traffic light color: ")

if selected_option == "Red":
    print("Stop!")
elif selected_option == "Green":
    print("Go!")
elif selected_option == "Yellow":
    print("Get ready!")
else:
    print("Invalid option")

# 7. Ternary Operator
# Instead of writing
is_account_suspended = True

if is_account_suspended:
    status = "Account is suspended"
else:
    status = "Account is active"

# you can write
status = "Account is suspended" if is_account_suspended else "Account is active"

print(status)

# 8. Task Completion Example
total_tasks = 10
completed_tasks = int(input("No of tasks completed: "))
status = "completed" if total_tasks == completed_tasks else "In progress"
print(status)
