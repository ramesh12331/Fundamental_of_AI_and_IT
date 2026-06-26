Here's a professional **README.md** version of your **Python Variables & Data Types** notes. It is structured for GitHub, interview preparation, and beginner-friendly learning.

# 🐍 Python Variables & Data Types – Complete Interview Notes

> A comprehensive guide to Python variables, data types, lists, dictionaries, dynamic typing, and commonly asked interview questions.

---

# 📚 Table of Contents

* Introduction
* Variables
* Printing Variables
* `type()` Function
* Primitive Data Types

  * Integer (`int`)
  * Float (`float`)
  * String (`str`)
  * Boolean (`bool`)
* Multi-line Strings
* Data Type Categories
* Dynamic Typing
* Static vs Dynamic Data
* Lists
* List Operations
* Dictionaries
* List vs Dictionary
* Best Practices
* Frequently Asked Interview Questions
* Final Summary

---

# 🐍 Introduction

Variables and data types are the foundation of Python programming. Variables store values, while data types define the kind of data those variables can hold.

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
email = "support@datavalley.ai"
password = "Test@123"
pin_code = 500001
company_name = "Datavalley"
bank_balance = 52900.56
is_account_active = True
```

---

# 🖨️ Printing Variables

Use the `print()` function to display variable values.

```python
print("Email Address:", email)
print(pin_code)
print(bank_balance)
```

### Output

```text
Email Address: support@datavalley.ai
500001
52900.56
```

---

# 🔍 The `type()` Function

The `type()` function returns the data type of a variable.

```python
email = "support@datavalley.ai"
pin_code = 500001
bank_balance = 52900.56
is_account_active = True

print(type(pin_code))
print(type(bank_balance))
print(type(email))
print(type(is_account_active))
```

### Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# 📊 Primitive Data Types

## 1️⃣ Integer (`int`)

Stores whole numbers.

```python
price = 5600

print(price)
print(type(price))
```

### Output

```text
5600
<class 'int'>
```

---

## 2️⃣ Float (`float`)

Stores decimal numbers.

```python
rating = 4.3

print(type(rating))
```

### Output

```text
<class 'float'>
```

---

## 3️⃣ String (`str`)

Stores text enclosed in quotes.

### Double Quotes

```python
device = "Datavalley's Laptop"

print(device)
```

### Output

```text
Datavalley's Laptop
```

### Another Example

```python
device = "Dinesh's iPhone"

print(device)
```

### Output

```text
Dinesh's iPhone
```

> **Tip:** If the string contains an apostrophe (`'`), wrap it in double quotes (`"`).

---

## 4️⃣ Boolean (`bool`)

Stores only two values.

```python
is_account_active = True

print(type(is_account_active))
```

### Output

```text
<class 'bool'>
```

Possible values:

```python
True
False
```

---

# 📝 Multi-line Strings

Triple quotes (`'''` or `"""`) allow strings to span multiple lines.

```python
message = """
Snake case is a naming convention.
It uses lowercase letters.
Words are separated using underscores.
"""

print(message)
```

### Output

```text
Snake case is a naming convention.
It uses lowercase letters.
Words are separated using underscores.
```

---

# 🗂️ Python Data Type Categories

Python's built-in data types can be grouped into two categories.

## Primitive (Simple) Types

Store a single value.

| Data Type | Example    |
| --------- | ---------- |
| `int`     | `10`       |
| `float`   | `4.5`      |
| `str`     | `"Python"` |
| `bool`    | `True`     |

---

## Collection Types

Store multiple values.

| Collection Type | Description                           |
| --------------- | ------------------------------------- |
| List            | Ordered, mutable collection           |
| Tuple           | Ordered, immutable collection         |
| Set             | Unordered collection of unique values |
| Dictionary      | Key-value pairs                       |

---

# ⚡ Dynamic Typing

Python automatically determines the data type at runtime.

```python
value = 100

print(type(value))
```

Output

```text
<class 'int'>
```

Later:

```python
value = "Python"

print(type(value))
```

Output

```text
<class 'str'>
```

This flexibility is known as **dynamic typing**.

---

# 🔄 Static vs Dynamic Data

## Static Data

Data that rarely changes.

Examples:

* Country Name
* Date of Birth
* PAN Number

```python
country = "India"
```

---

## Dynamic Data

Data that changes frequently.

Examples:

* Bank Balance
* Temperature
* Product Price
* Stock Price

```python
bank_balance = 52900.56

bank_balance = 54120.75
```

---

# 📋 Lists

## Definition

A **List** is an ordered, mutable collection that stores multiple values.

### Properties

* Ordered
* Mutable
* Allows duplicate values
* Indexed (zero-based)

### Syntax

```python
employees = ["Lokesh", "Ganesh", "Charan", "Naveen"]
```

---

# 🔢 List Indexing

Python lists use **zero-based indexing**.

```text
Index:       0         1         2         3
          -------------------------------------
employees = ["Lokesh","Ganesh","Charan","Naveen"]
```

---

# 📥 Accessing Elements

```python
print(employees[0])
```

Output

```text
Lokesh
```

```python
print(employees[2])
```

Output

```text
Charan
```

---

# 📏 Length of a List

Use `len()` to find the number of elements.

```python
print(len(employees))
```

Output

```text
4
```

---

# 🔁 Duplicate Values

Lists allow duplicate values.

```python
employees = [
    "Lokesh",
    "Ganesh",
    "Charan",
    "Naveen",
    "Naveen",
    "Charan"
]

print(employees)
```

Output

```text
['Lokesh', 'Ganesh', 'Charan', 'Naveen', 'Naveen', 'Charan']
```

---

# ❌ Removing an Item

The `remove()` method deletes the **first matching value**.

```python
employees.remove("Naveen")

print(employees)
```

Output

```text
['Lokesh', 'Ganesh', 'Charan', 'Naveen', 'Charan']
```

---

# 🤔 Why Use a List?

Instead of multiple variables:

```python
employee1 = "Lokesh"
employee2 = "Ganesh"
employee3 = "Charan"
employee4 = "Naveen"
```

Use a single list:

```python
employees = ["Lokesh", "Ganesh", "Charan", "Naveen"]
```

Benefits:

* Easier to manage
* Easier to loop through
* Cleaner code
* Scalable

---

# 📖 Dictionaries

## Definition

A **Dictionary** stores data as **key-value pairs**.

### Properties

* Mutable
* Keys are unique
* Fast lookup by key
* Preserves insertion order (Python 3.7+)

### Syntax

```python
product_info = {
    "name": "realme NARZO 80 Pro 5G",
    "avg_rating": 4.3,
    "rating_count": 2600,
    "discount": 14,
    "price": 27999
}
```

---

# 🔑 Accessing Dictionary Values

```python
print(product_info["avg_rating"])
```

Output

```text
4.3
```

```python
print(product_info["price"])
```

Output

```text
27999
```

---

# ⚖️ List vs Dictionary

| List                    | Dictionary                              |
| ----------------------- | --------------------------------------- |
| Stores values           | Stores key-value pairs                  |
| Access using index      | Access using key                        |
| Allows duplicate values | Keys must be unique                     |
| Ordered                 | Preserves insertion order (Python 3.7+) |

---

# 🌟 Best Practices

* Use meaningful variable names.
* Follow `snake_case` naming conventions.
* Use lists for ordered collections of similar items.
* Use dictionaries for structured key-value data.
* Prefer double quotes when strings contain apostrophes.
* Use `type()` while learning to verify data types.

---

# 🎤 Frequently Asked Interview Questions

### 1. What is a variable?

A named container used to store data in memory.

---

### 2. What does `type()` do?

It returns the data type of a variable.

---

### 3. What are the four primitive data types in Python?

* `int`
* `float`
* `str`
* `bool`

---

### 4. What is dynamic typing?

Python automatically determines the data type of a variable during execution, allowing the same variable to store different types.

---

### 5. What is a list?

A mutable, ordered collection that stores multiple values and allows duplicate elements.

---

### 6. What is a dictionary?

A mutable collection that stores data as key-value pairs and provides fast access using keys.

---

### 7. Difference Between a List and a Dictionary?

| List                  | Dictionary                    |
| --------------------- | ----------------------------- |
| Uses indexes          | Uses keys                     |
| Example: `["A", "B"]` | Example: `{"name": "Ramesh"}` |
| Access: `list[0]`     | Access: `dict["name"]`        |

---

# 🖼️ Reference Diagrams

## Variable Assignment

```text
email = "support@datavalley.ai"

Variable (email)
        │
        ▼
"support@datavalley.ai"
```

---

## Python Data Types

```text
Python Data Types
        │
 ┌──────┴──────────┐
 │                 │
 ▼                 ▼
Primitive      Collection
 │                 │
 ├── int          ├── List
 ├── float        ├── Tuple
 ├── str          ├── Set
 └── bool         └── Dictionary
```

---

## List Structure

```text
Index:       0         1         2         3
          -------------------------------------
employees = ["Lokesh","Ganesh","Charan","Naveen"]
```

---

## Dictionary Structure

```text
product_info
      │
      ├── name           → realme NARZO 80 Pro 5G
      ├── avg_rating     → 4.3
      ├── rating_count   → 2600
      ├── discount       → 14
      └── price          → 27999
```

---

# 📌 Final Summary

* Variables are named containers used to store data in memory.
* Python provides four primitive data types: **int**, **float**, **str**, and **bool**.
* Collection data types include **list**, **tuple**, **set**, and **dictionary**.
* The `type()` function helps identify the data type of a value or variable.
* Python uses **dynamic typing**, so variable types are determined at runtime.
* Lists are ideal for ordered collections of items, while dictionaries are best for storing structured data as key-value pairs.
* Mastering variables, data types, lists, and dictionaries is essential for writing effective Python programs and succeeding in Python interviews.

### 📖 Recommended Reference Images

To enhance your README, include these visuals:

![Image](https://images.openai.com/static-rsc-4/1pTGm4ugVlFdx38cZ_zc4-pGUxITlhjDjB9ua04cNipCTk7CYSdEBIqAmFlq37EDFTw7H6l9SNCb0Jvp2qG70fhTRsWzGnbsI7gh0t2cTVAePa4EWnFGC9y2IEUOVWTeYKwOJ-ALHFZpUhP2J17EENRAANiXsW6dAJvlgcAMlvoSmM4ssUmobkRZM_cCQbUb?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/30RsVodvG3r66YXZb3BGdutaB_p205E1mdEpy1CijtjEfH0ff3LHj45WM2JJ0brp2o2Aqa-ufVarRPa0LqqccrBYLARUe1UMwpai8wU_jSRsHab7wPiy-yr9pzhRWTIpR_SOW-DSHA3xMq1BdPbrrbnSFX9B_2Nl6ad_xc9l9TAMMBEc2-jZsmoVAdgIQVzM?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/U4dxRzunf6Xggs_w-yiJCfEsvum5ylxaJ68AamTRWB_IRfnDSJ6uebQIEGIO_QMj_-s1qUHYBHf_6_52srjuZTC4kMCS_v09xTxpPHduk527WsBh8hrNrh7TSrUzwFZBoPxAW3J7V9oTh38wPnqekGCI6RwSE5dRehtghG7vZlN2N4Qo5ljYDApJjBcJW9bh?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/WFIDfwpcSwIQ6UnTYphpUZu3-QSdq_I89RfXaqbn_filN4hRnSLjcrbPKP8_2tXNsyL4ahwyMw1WEjayhN-6e7f09PT7sNDrpykdfzw4BshJq8g4JCZ62EyCWDgel0FtIlxi0Zz5z2rZhA9brx6UnFGucH5kUv_ASSNqDSRF9QFYHVI65y9gnv3llIgRUXxs?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/_cqzYW-z7jQk3ZXFc8gRWlSkqIlOsg1pAYRAzCu9gno-GA0txrJvo1L7RbUyO2ekE6doTJsfO1halEiCmDl68hzE8Bp8i8nG1pgKEVx1JNXbPyntMgIr7HR0DFFqZQ9k1tzWDzrCYjGYHEa19WV7LiCL3bddATkw1lLmBF6c8mQz5O91OvVpPAczsvmIgfYk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/NSZ-Oz3jqIz5LI2wZ_XOhOfwITJpgsBRunZgN_OX4K-_KQkVbxyBB3FplTHRyDcc7E6J4zIFA4Qb16VleyOKftJAeJtJPuQ_DGdQ4ikxgsvANQB-r4KOfzb37QkJe4gKlXQDwf_XADHo3YABiwBQSxODrVz99tbzqttjx0HPKIU-vP2Dz-I3b_eUl-XKzfeJ?purpose=fullsize)

These diagrams help visualize variable assignment, built-in data types, list indexing, and dictionary key-value mappings, making the notes more engaging and easier to understand.
