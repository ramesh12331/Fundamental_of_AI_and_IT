# 🐍 Python Conditional Statements & Ternary Operator

> **Complete Beginner to Interview Guide** covering User Input, Type Conversion, Conditional Statements (`if`, `if-else`, `if-elif-else`), Boolean Values, Truthy & Falsy, Ternary Operator, and List of Dictionaries.

---

# 📚 Table of Contents

* Introduction
* User Input & Type Conversion
* `if` Statement
* Boolean Example
* ATM Withdrawal Program
* Login Validation Using Dictionary
* Truthy & Falsy Values
* `if-elif-else` Statement
* Traffic Signal Program
* Ternary Operator
* Task Completion Example
* List of Dictionaries
* Best Practices
* Frequently Asked Interview Questions
* Reference Diagrams
* Final Summary

---

# 📖 Introduction

Conditional statements help a program make decisions based on conditions.

Python supports:

* `if`
* `if-else`
* `if-elif-else`
* Ternary Operator (Conditional Expression)

These concepts are widely used in real-world applications like login systems, ATM software, shopping carts, and dashboards.

---

# ⌨️ User Input & Type Conversion

The `input()` function accepts data from the keyboard.

## Syntax

```python
variable = input("Enter value: ")
```

> **Important:** `input()` always returns a **string (`str`)**.

---

## Problem

```python
age = input("Enter your age: ")

if age > 18:
    print("You are eligible to vote!")
```

### Error

```text
TypeError: '>' not supported between instances of 'str' and 'int'
```

### Why?

```python
age = input("22")
```

actually stores:

```python
age = "22"
```

Python cannot compare:

```python
"22" > 18
```

---

## Correct Code

```python
age = int(input("Enter your age: "))

if age > 18:
    print("You are eligible to vote!")
```

### Output

```text
Enter your age: 22
You are eligible to vote!
```

---

# ✅ Boolean Example

Boolean values contain only:

* `True`
* `False`

### Example

```python
is_account_activated = False

if is_account_activated:
    print("Your account is in active state")
else:
    print("Your account is in deactivated state")
```

### Output

```text
Your account is in deactivated state
```

### Explanation

Since the value is `False`, the `else` block executes.

---

# 🏧 ATM Withdrawal Program

### Example

```python
balance = 4500

amount = float(input("Enter the amount: "))

if balance >= amount:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance is {balance}")
else:
    print("Insufficient balance")
```

---

## Example 1

### Input

```text
2356
```

### Output

```text
Withdrawal successful!
Remaining balance is 2144.0
```

---

## Example 2

### Input

```text
4900
```

### Output

```text
Insufficient balance
```

---

### Explanation

The withdrawal succeeds only when:

```python
balance >= amount
```

Otherwise, the transaction is rejected.

---

# 🔐 Login Validation Using Dictionary

```python
user = {
    "name": "Charan",
    "email": "charan90@gmail.com",
    "password": "Charan@24"
}

entered_email = input("Enter email: ")
entered_password = input("Enter password: ")

if (
    entered_email == user["email"]
    and
    entered_password == user["password"]
):
    print("Credentials are valid")
else:
    print("Incorrect email or password")
```

---

## Correct Input

```text
charan90@gmail.com
Charan@24
```

Output

```text
Credentials are valid
```

---

## Incorrect Input

```text
charan90@datavalley.ai
Charan@24
```

Output

```text
Incorrect email or password
```

---

# ⚡ Truthy & Falsy Values

Python evaluates values as **True** or **False** in conditional statements.

---

## Falsy Values

```python
False
None
0
0.0
""
[]
{}
set()
```

---

## Truthy Values

```python
5
-100
2.5
"Python"
[1,2]
{"name":"Rahul"}
True
```

---

### Example

```python
balance = -100

if balance:
    print("Status")
```

Output

```text
Status
```

---

### Example

```python
if 0:
    print("Hello")
```

Output

```text
Nothing is printed
```

---

### Example

```python
if -10:
    print("Hello")
```

Output

```text
Hello
```

---

# 🚦 if-elif-else Statement

Used when multiple conditions need to be checked.

---

## Traffic Signal Program

```python
selected_option = input("Enter traffic light color: ")

if selected_option == "Red":
    print("Stop!")

elif selected_option == "Yellow":
    print("Get ready!")

elif selected_option == "Green":
    print("Go!")

else:
    print("Invalid option")
```

---

### Input

```text
Red
```

Output

```text
Stop!
```

---

### Input

```text
Yellow
```

Output

```text
Get ready!
```

---

### Input

```text
Green
```

Output

```text
Go!
```

---

# ⚡ Ternary Operator

The ternary operator writes a simple `if-else` in one line.

---

## Syntax

```python
value_if_true if condition else value_if_false
```

---

## Example

```python
is_account_suspended = True

status = (
    "Account is suspended"
    if is_account_suspended
    else "Account is active"
)

print(status)
```

Output

```text
Account is suspended
```

---

If

```python
is_account_suspended = False
```

Output

```text
Account is active
```

---

# 📋 Task Completion Example

```python
total_tasks = 10

completed_tasks = int(input("No of tasks completed: "))

status = (
    "Completed"
    if total_tasks == completed_tasks
    else "In-progress"
)

print(status)
```

---

### Input

```text
10
```

Output

```text
Completed
```

---

### Input

```text
8
```

Output

```text
In-progress
```

---

# 📚 List of Dictionaries

A list can contain multiple dictionaries.

Each dictionary stores one employee record.

```python
employees = [
    {
        "employee_id":101,
        "name":"Rahul Sharma",
        "department":"IT",
        "designation":"Software Engineer",
        "salary":75000,
        "experience":3,
        "location":"Hyderabad"
    },
    {
        "employee_id":102,
        "name":"Priya Reddy",
        "department":"HR",
        "designation":"HR Manager",
        "salary":68000,
        "experience":5,
        "location":"Bangalore"
    }
]
```

---

## Access Dictionary Values

```python
print(employees[0]["name"])
```

Output

```text
Rahul Sharma
```

---

```python
print(employees[1]["salary"])
```

Output

```text
68000
```

---

# 🌟 Best Practices

* Convert numeric input using `int()` or `float()`.
* Use meaningful variable names.
* Keep conditions readable.
* Store structured data using dictionaries.
* Use `if-elif-else` for multiple conditions.
* Use the ternary operator only for simple conditions.
* Follow Python's 4-space indentation rule.

---

# 🎤 Frequently Asked Interview Questions

### 1. Why does `input()` require `int()` or `float()`?

Because `input()` always returns a string.

---

### 2. What are Boolean values?

Boolean values are:

* `True`
* `False`

---

### 3. What are Truthy and Falsy values?

Falsy values evaluate to `False`, while all other values are considered Truthy.

---

### 4. What is the difference between `if`, `if-else`, and `if-elif-else`?

| Statement      | Purpose                                     |
| -------------- | ------------------------------------------- |
| `if`           | Executes code only if the condition is True |
| `if-else`      | Chooses between two blocks                  |
| `if-elif-else` | Handles multiple conditions                 |

---

### 5. What is the ternary operator?

A one-line shorthand for a simple `if-else` statement.

---

### 6. Why use dictionaries?

Dictionaries store related information as key-value pairs and allow fast lookup using keys.

---

### 7. What is a List of Dictionaries?

A collection where each list element is a dictionary representing one record.

---

# 📊 Reference Diagrams

## User Input Flow

```text
Keyboard
    │
    ▼
 input()
    │
    ▼
 String
    │
 int()/float()
    │
    ▼
 Number
```

---

## Conditional Flow

```text
Condition
    │
    ▼
 True?
 ┌──┴──┐
 │     │
Yes    No
 │     │
 ▼     ▼
Block  Else Block
```

---

## if-elif-else Flow

```text
Condition 1
     │
 True?
 ┌──┴────┐
 │       │
Yes     No
 │       │
 ▼    Condition 2
          │
       True?
      ┌──┴──┐
      │     │
     Yes   No
      │     │
      ▼     ▼
   Block2  Else
```

---

## ATM Flow

```text
Enter Amount
      │
      ▼
Balance >= Amount?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Withdraw  Insufficient Balance
```

---

## Login Validation

```text
Enter Email & Password
        │
        ▼
Credentials Match?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Login   Invalid Credentials
```

---

# 📌 Final Summary

| Concept              | Purpose                               |
| -------------------- | ------------------------------------- |
| `input()`            | Accept user input                     |
| `int()` / `float()`  | Convert strings into numbers          |
| `if`                 | Execute code when a condition is True |
| `if-else`            | Choose between two blocks             |
| `if-elif-else`       | Handle multiple conditions            |
| Boolean              | Represent True or False               |
| Truthy & Falsy       | Control conditional execution         |
| Dictionary           | Store related key-value data          |
| Logical `and`        | Combine multiple conditions           |
| Ternary Operator     | Write simple `if-else` in one line    |
| List of Dictionaries | Store multiple structured records     |

## ✅ Key Takeaways

* `input()` always returns a string, so convert numeric input before comparisons.
* Conditional statements help programs make decisions.
* Dictionaries are commonly used for storing user and application data.
* Truthy and Falsy values determine how conditions are evaluated.
* The ternary operator makes simple conditional assignments concise.
* Lists of dictionaries are widely used in real-world applications such as employee management systems and APIs.
* These topics are essential Python fundamentals and are frequently asked in beginner interviews and coding assessments.

---
# 🐍 Python Loops & Nested Data Structures

> **Complete Interview Notes** covering Lists of Dictionaries, Dictionary Iteration, `range()`, `while` Loop, and Employee Login System with Examples.

---

# 📚 Table of Contents

* List of Dictionaries
* Loop Through List of Dictionaries
* Print Employee Details
* Separator Line
* Loop Through Tuple
* Loop Through String
* Dictionary `items()`
* Loop Through Dictionary
* `range()` Function
* `while` Loop
* Employee Login Attempts
* Dry Run
* Best Practices
* Interview Questions
* Final Summary

---

# 📖 List of Dictionaries

## Definition

A **List of Dictionaries** stores multiple records where each dictionary represents a single object such as an employee, student, or product.

### Features

* Stores multiple records
* Each record is a dictionary
* Easy to iterate using loops
* Commonly used in APIs and databases

---

## Example

```python
employees = [
    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "IT",
        "designation": "Software Engineer",
        "salary": 75000,
        "experience": 3,
        "location": "Hyderabad"
    },
    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "HR",
        "designation": "HR Manager",
        "salary": 68000,
        "experience": 5,
        "location": "Bangalore"
    }
]
```

---

# 🔄 Print Every Dictionary

```python
for employee in employees:
    print(employee)
```

### Output

```
{'employee_id':101,'name':'Rahul Sharma',...}
{'employee_id':102,'name':'Priya Reddy',...}
```

### Explanation

* `employee` stores one dictionary at a time.
* `print(employee)` prints the complete dictionary.

---

# 👨‍💼 Print Employee Number

```python
i = 1

for employee in employees:
    print("Employee:", i)
    print(employee)
    i += 1
```

---

# 📋 Print Employee Details

```python
i = 1

for employee in employees:

    print("-" * 30)
    print("Employee:", i)

    print(f"Employee ID : {employee['employee_id']}")
    print(f"Name        : {employee['name']}")
    print(f"Department  : {employee['department']}")
    print(f"Designation : {employee['designation']}")
    print(f"Salary      : {employee['salary']}")
    print(f"Experience  : {employee['experience']}")
    print(f"Location    : {employee['location']}")

    i += 1
```

---

# ➖ Separator Line

```python
print("-" * 30)
```

### Output

```
------------------------------
```

Useful for displaying multiple employee records neatly.

---

# 📅 Loop Through Tuple

```python
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
)

for month in months:
    print(month)
```

---

# 🔤 Loop Through String

```python
company_name = "Data Valley"

for char in company_name:
    print(char)
```

### Output

```
D
a
t
a

V
a
l
l
e
y
```

### Explanation

A string is a sequence of characters.

The loop prints one character at a time.

---

# 📖 Dictionary `items()`

```python
employee_info = {
    "employee_id":101,
    "name":"Rahul Sharma",
    "department":"IT"
}

print(employee_info.items())
```

### Output

```
dict_items([
('employee_id',101),
('name','Rahul Sharma'),
('department','IT')
])
```

---

# 🔑 Loop Through Dictionary

```python
for key, value in employee_info.items():
    print(key, value)
```

### Output

```
employee_id 101
name Rahul Sharma
department IT
```

---

# 🔁 Another Way

```python
for item in employee_info.items():
    print(item)
    print(item[0], item[1])
```

### Output

```
('employee_id',101)
employee_id 101

('name','Rahul Sharma')
name Rahul Sharma
```

---

# 🔢 `range()` Function

The `range()` function generates a sequence of numbers.

```python
for i in range(0, 5):
    print("In for loop")
```

### Output

```
In for loop
In for loop
In for loop
In for loop
In for loop
```

---

# 📋 `range()` with List

```python
colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Orange"
]

for i in range(len(colors)):
    print(colors[i])
```

---

# 🔄 `while` Loop

```python
counter = 0

while counter < 5:
    print("Counter:", counter)
    counter += 1
```

### Output

```
Counter: 0
Counter: 1
Counter: 2
Counter: 3
Counter: 4
```

---

# 🔐 Employee Login Attempts

```python
employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "pin": "3450",
    "department": "IT"
}

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    entered_employee_id = int(input("Enter Employee ID: "))
    entered_pin = input("Enter PIN: ")

    if (
        entered_employee_id == employee_info["employee_id"]
        and
        entered_pin == employee_info["pin"]
    ):
        print("Credentials are correct")
        break

    else:
        attempts += 1
        print(f"Invalid credentials, {max_attempts-attempts} attempts left")

if attempts == max_attempts:
    print("Account Locked!")
```

---

# 🧪 Sample Output

```
Enter Employee ID: 45
Enter PIN: 45678

Invalid credentials, 2 attempts left

Enter Employee ID: 101
Enter PIN: 3450

Credentials are correct
```

---

# 🔍 Dry Run

| Attempt | Employee ID | PIN   |   Result  | Remaining Attempts |
| ------: | ----------- | ----- | :-------: | -----------------: |
|       1 | 45          | 45678 | ❌ Invalid |                  2 |
|       2 | 101         | 3450  | ✅ Success |   Login Successful |

---

# 🌟 Best Practices

* Store structured records using **List of Dictionaries**.
* Use `items()` to iterate through dictionary key-value pairs.
* Use `range()` when indexes are required.
* Use `while` loops for retry mechanisms such as login systems.
* Convert numeric input using `int()` or `float()`.
* Use `break` to exit a loop after a successful operation.

---

# 🎤 Frequently Asked Interview Questions

### 1. What is a List of Dictionaries?

A collection where each list element is a dictionary representing one record.

---

### 2. What does `items()` return?

It returns all dictionary key-value pairs as tuples.

---

### 3. Why use `range(len(list))`?

To iterate using list indexes.

---

### 4. Why use a `while` loop for login systems?

Because login attempts depend on a condition rather than a fixed number of iterations.

---

### 5. What does `break` do?

It immediately exits the loop.

---

### 6. Why convert `input()` using `int()`?

Because `input()` always returns a string, but numeric comparisons require integers.

---

# 📊 Reference Diagrams

## List of Dictionaries

```text
employees
│
├── Dictionary 1
│      ├── employee_id
│      ├── name
│      └── department
│
├── Dictionary 2
│
└── Dictionary 3
```

---

## Dictionary Iteration

```text
employee_info.items()

        │
        ▼

(employee_id,101)
(name,Rahul Sharma)
(department,IT)
```

---

## while Loop

```text
Start
 │
 ▼
Condition
 │
 ▼
True?
 │      │
Yes     No
 │       ▼
 ▼      End
Execute
 │
 ▼
Update Counter
 │
 └────────────►
```

---

## Employee Login Flow

```text
Start
 │
 ▼
Enter Employee ID & PIN
 │
 ▼
Credentials Correct?
 │
├── Yes → Login Success → End
│
└── No
      │
      ▼
Increase Attempts
      │
      ▼
Attempts < 3 ?
      │
 ┌────┴────┐
 │         │
Yes       No
 │         │
 ▼         ▼
Retry   Account Locked
```

---

# 📌 Final Summary

| Concept              | Purpose                                |
| -------------------- | -------------------------------------- |
| List of Dictionaries | Store multiple structured records      |
| `for` Loop           | Iterate through collections            |
| `items()`            | Access dictionary key-value pairs      |
| `range()`            | Generate sequences or indexes          |
| `while` Loop         | Repeat until a condition becomes False |
| `break`              | Exit a loop immediately                |

## ✅ Key Takeaways

* Lists of dictionaries are widely used in real-world applications to represent employees, products, students, and customers.
* Use `for` loops to iterate over collections efficiently.
* The `items()` method simplifies dictionary traversal.
* `while` loops are ideal for retry-based workflows such as login systems.
* Always convert user input to the appropriate data type before comparisons.
* These topics are frequently asked in Python interviews and are essential for building real-world applications.
