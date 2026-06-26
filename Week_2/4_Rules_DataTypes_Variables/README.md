Below is a professional **README.md** document for **Python Basics**. It is organized for beginners, interview preparation, and GitHub documentation.

# 🐍 Python Basics – Complete Interview Notes

> A beginner-friendly guide covering Python syntax, variables, data types, lists, dynamic typing, and common interview questions.

---

# 📚 Table of Contents

* Introduction
* Python Syntax Rules
* Running Python Programs
* Variables
* Variable Naming (snake_case)
* Data Types
* Dynamic Typing
* Static vs Dynamic Data
* Lists
* List Indexing
* Common `type()` Examples
* Best Practices
* Frequently Asked Interview Questions
* Final Summary

---

# 🐍 Introduction

Python is a **high-level**, **interpreted**, **general-purpose** programming language known for its simple syntax and readability.

It is widely used in:

* Web Development
* Automation
* Artificial Intelligence
* Machine Learning
* Data Science
* API Development
* Cyber Security

---

# 📖 Python Syntax Rules

Python follows strict syntax rules to ensure code is readable and executable.

---

## Rule 1: Statements Begin at the Start of the Line

Each statement starts at the beginning of the line unless it belongs to a code block.

```python
a = 10
b = 20

print(a + b)
```

**Output**

```text
30
```

---

## Rule 2: Use a Colon (`:`) Before a Code Block

Statements that expect nested code must end with a colon.

```python
if age > 30:
    print("Age is greater than 30")
```

Examples:

```python
if age > 30:
for i in range(5):
while True:
def add():
class Employee:
```

---

## Rule 3: Use Indentation

Python uses indentation instead of curly braces (`{}`) to define blocks of code.

```python
if age > 30:
    print("Age is greater than 30")
```

---

## Rule 4: Keep Indentation Consistent

✔ Correct

```python
if age > 30:
    print("Adult")
    print("Eligible")
```

❌ Incorrect

```python
if age > 30:
    print("Adult")
       print("Eligible")
```

This causes an **IndentationError**.

---

# ▶️ Running Python Programs

Run a Python file from the terminal:

```bash
python app.py
```

Display output using the `print()` function:

```python
print(45 + 45)
```

**Output**

```text
90
```

---

# 📦 Variables

## Definition

A **variable** is a named container used to store data in memory.

### Syntax

```python
variable_name = value
```

### Example

```python
age = 25
name = "Ramesh"
salary = 45000
```

The `=` operator assigns the value on the right to the variable on the left.

---

# 📝 Variable Naming (snake_case)

Python follows the **snake_case** naming convention recommended by **PEP 8**.

### Rules

* Use lowercase letters.
* Separate words with underscores (`_`).
* Choose meaningful names.

✔ Correct

```python
employee_name
student_age
total_salary
```

❌ Incorrect

```python
EmployeeName
employeeName
EMPLOYEENAME
```

---

# 📊 Data Types

A **data type** defines the kind of value stored in a variable.

---

## 1️⃣ Integer (`int`)

Stores whole numbers.

```python
age = 25
print(type(age))
```

Output

```text
<class 'int'>
```

---

## 2️⃣ Float (`float`)

Stores decimal numbers.

```python
price = 99.99
print(type(price))
```

Output

```text
<class 'float'>
```

---

## 3️⃣ String (`str`)

Stores text enclosed in quotes.

```python
name = "Ramesh"
print(type(name))
```

Output

```text
<class 'str'>
```

---

## 4️⃣ Boolean (`bool`)

Stores one of two values: `True` or `False`.

```python
is_active = True
print(type(is_active))
```

Output

```text
<class 'bool'>
```

---

# 📚 Collection Data Types

Python also provides built-in collection types to store multiple values.

| Data Type  |     Ordered     | Mutable |  Allows Duplicates  |
| ---------- | :-------------: | :-----: | :-----------------: |
| List       |        ✅        |    ✅    |          ✅          |
| Tuple      |        ✅        |    ❌    |          ✅          |
| Set        |        ❌        |    ✅    |          ❌          |
| Dictionary | ✅ (Python 3.7+) |    ✅    | Keys must be unique |

---

# ⚡ Dynamic Typing

Python is **dynamically typed**, meaning the interpreter determines the data type automatically at runtime.

```python
value = 10
print(type(value))
```

Output

```text
<class 'int'>
```

Later, the same variable can hold a different type.

```python
value = "Hello"
print(type(value))
```

Output

```text
<class 'str'>
```

---

# 🔄 Static vs Dynamic Data

## Static Data

Values that rarely change.

Example:

```python
country = "India"
```

---

## Dynamic Data

Values that can change during program execution.

Example:

```python
temperature = 35

temperature = 38
```

---

# 📋 Lists

## Definition

A **List** is an ordered, mutable collection used to store multiple values.

### Features

* Ordered
* Mutable (can be modified)
* Allows duplicate values
* Zero-based indexing

### Syntax

```python
employees = ["Ramesh", "Lakshmi", "Ram"]
```

---

# 🔢 List Indexing

Python uses **zero-based indexing**.

```text
Index:        0          1          2
           --------------------------------
employees = ["Ramesh", "Lakshmi", "Ram"]
```

### Access First Element

```python
employees[0]
```

Output

```text
Ramesh
```

### Access Third Element

```python
employees[2]
```

Output

```text
Ram
```

---

# ❌ List Index Error

Trying to access an index outside the valid range raises an `IndexError`.

```python
employees = ["Ramesh", "Lakshmi", "Ram"]

print(employees[4])
```

Output

```text
IndexError: list index out of range
```

---

# 🔍 Common `type()` Examples

```python
print(type(10))
# <class 'int'>

print(type(10.5))
# <class 'float'>

print(type("Python"))
# <class 'str'>

print(type(True))
# <class 'bool'>
```

---

# 🌟 Best Practices

* Use meaningful variable names.
* Follow `snake_case` naming.
* Keep indentation consistent (4 spaces).
* Avoid hardcoded values where possible.
* Use `type()` to understand data types while learning.
* Write readable and well-commented code.

---

# 🎤 Frequently Asked Interview Questions

### 1. What is a variable?

A variable is a named container used to store data in memory.

---

### 2. What is `snake_case`?

A naming convention where words are written in lowercase and separated by underscores, such as `employee_name`.

---

### 3. What are the basic Python data types?

* `int`
* `float`
* `str`
* `bool`

---

### 4. What is dynamic typing?

Python automatically determines a variable's data type at runtime, allowing the same variable to store different types during execution.

---

### 5. What is a list?

A list is an ordered, mutable collection that stores multiple values and allows duplicate elements.

---

### 6. What is list indexing?

List elements are accessed using zero-based indexes (`0`, `1`, `2`, ...).

---

### 7. Why does `IndexError: list index out of range` occur?

It occurs when attempting to access an index that does not exist in the list.

---

### 8. What is the difference between `int` and `float`?

| `int`                | `float`                |
| -------------------- | ---------------------- |
| Stores whole numbers | Stores decimal numbers |
| Example: `25`        | Example: `25.5`        |

---

### 9. What is the difference between mutable and immutable?

| Mutable                       | Immutable                        |
| ----------------------------- | -------------------------------- |
| Can be changed after creation | Cannot be changed after creation |
| Example: List                 | Example: Tuple, String           |

---

# 🖼️ Reference Diagrams

## Python Program Execution Flow

```text
Write Code
     │
     ▼
Save File (.py)
     │
     ▼
Run Program
     │
     ▼
Python Interpreter
     │
     ▼
Output
```

---

## Variable Assignment

```text
age = 25

Variable (age)
      │
      ▼
    Value (25)
```

---

## Python Data Types

```text
Python Data Types
        │
 ┌──────┴──────────┐
 │                 │
 ▼                 ▼
Simple        Collection
 │                 │
 ├── int           ├── List
 ├── float         ├── Tuple
 ├── str           ├── Set
 └── bool          └── Dictionary
```

---

## List Indexing

```text
Index:      0          1          2
          ----------------------------
employees = ["Ramesh","Lakshmi","Ram"]
```

---

# 📌 Final Summary

* Python uses **indentation** to define code blocks instead of curly braces.
* Variables store data and are assigned using the `=` operator.
* Follow **snake_case** naming conventions for readable code.
* Python's basic data types include **int**, **float**, **str**, and **bool**.
* Collection data types include **list**, **tuple**, **set**, and **dictionary**.
* Python is **dynamically typed**, allowing variables to hold different data types during execution.
* Lists are ordered, mutable, support duplicate values, and use **zero-based indexing**.
* Understanding syntax, variables, data types, and lists is essential for Python programming and technical interviews.

### 📖 Suggested Reference Images

Add these diagrams to your README for better visualization:

![Image](https://images.openai.com/static-rsc-4/Q3S5_jFiJXGwwwMwDZr8sq5NYbn2JrC6JNeBm4nEbA1RbIQt7eWS5DDq6dBOjPALjOxhapzc-uH1xjY9WiafqutgYkSbNBxILyrGFnW-A0cdzr9XrBnjhOFSwNLIHawVUQeTOfmAc0na3wiNz5E6vONl_qOw8P_kUaPMKL1QISXorBhzOUcBlNBuS7S1jqpz?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/b3rrj0I7UaQYI4PSflRuq4xzdgiwLZUViEA76sR0XJvbR2O13iGIr-iW0ctJOeazxixGmOstvk_DvJBAxbQwXyJGd_Zy92PhDZBSNygdp-YCLj72j_eayERwwC-oni-k5orznihnLPna_SHENEO7OxV64edGwF_9wcPLEg6jBGzWnqUM90jUKfqNRPFI5K32?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/E9oI1ofgo54NyoGxZa5LRxKA25Qo3Napr1yI4bJb-VaOwoAVLRrzNKy5yO8AoieyhE6A8ijQo7gxRYZovxCs-mojcYt_VJJXp-YvKeAaH4aN4MkPqMGsWzB1S3CAfIYAaUz9Rm5JpxiWA0H6KoHrcRg2WL9UINMqzPU3X4AwCBMWFDlT-lcBYphhEyT0DTjs?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/mzeYn9yr8-cG5snCDFfqdKxJ4GtJOlqE_g-f5mE6kkJxkUcidak0srznCdWh-wzWJmKLS5LFOB2xeRaO2QZhYziuMkeTFFoqiiiiwggt8tFyhbS0gsvTuKzn46nWKL6TRN2jp13M5jeiSEncE80MCi_V7ZVJuB3SZKqxgxZwx3bPHfHPJB6oTQc6bFRN2-Mb?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/AUUrBg1LboM7-xns-PGV5nuXLkiQEIAJpCk6LbpF5DVnzGvWQ_Nt1JLOQoIKX1kT2_o9uSFwCKPIQfCdoGVHllmw9binOo8bczu7DdzpTb8Z2GJblQVgm8EKOgkzqwKjk-T9EzH-yOhXzFvkkIBfYx00xpKw5wERgLFCv1Z_nnHn9raUJpWaWOIlDPOdrts_?purpose=fullsize)

These images complement the notes by illustrating Python syntax, variable assignment, data types, list indexing, and the execution flow of a Python program.
