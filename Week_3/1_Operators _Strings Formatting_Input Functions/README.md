Below is a professional **README.md** section covering **Assignment Operators, Identity Operators, Membership Operators, Input Function, f-Strings, and Email Template**. It follows the same style as the previous Python notes.

# 🐍 Python Assignment, Identity & Membership Operators, Input, and f-Strings

> A beginner-friendly guide covering Assignment Operators, Identity Operators, Membership Operators, User Input, f-Strings, and Reusable Email Templates.

---

# 📚 Table of Contents

* Assignment Operators
* Identity Operators
* Membership Operators
* Input Function
* f-Strings
* Multi-line Strings
* Reusable Email Template
* Best Practices
* Frequently Asked Interview Questions
* Final Summary

---

# 📝 Assignment (Shorthand) Operators

## Definition

Assignment operators are used to **assign values** to variables and **update existing values**.

---

## Assignment Operators Table

| Operator | Description         | Example   | Equivalent       |
| -------- | ------------------- | --------- | ---------------- |
| `=`      | Assign value        | `a = 10`  | Assign 10 to `a` |
| `+=`     | Add and assign      | `a += 5`  | `a = a + 5`      |
| `-=`     | Subtract and assign | `a -= 5`  | `a = a - 5`      |
| `*=`     | Multiply and assign | `a *= 5`  | `a = a * 5`      |
| `/=`     | Divide and assign   | `a /= 5`  | `a = a / 5`      |
| `%=`     | Modulus and assign  | `a %= 5`  | `a = a % 5`      |
| `**=`    | Exponent and assign | `a **= 2` | `a = a ** 2`     |

---

## Examples

### Addition Assignment

```python
salary = 25000

salary += 5000

print(salary)
```

Output

```text
30000
```

---

### Multiplication Assignment

```python
marks = 20

marks *= 5

print(marks)
```

Output

```text
100
```

---

### Exponent Assignment

```python
number = 5

number **= 2

print(number)
```

Output

```text
25
```

---

# 🆔 Identity Operators

## Definition

Identity operators compare whether **two variables refer to the same object in memory**.

---

## Identity Operators Table

| Operator | Description                                               | Example      |
| -------- | --------------------------------------------------------- | ------------ |
| `is`     | Returns `True` if both variables refer to the same object | `a is b`     |
| `is not` | Returns `True` if variables refer to different objects    | `a is not b` |

---

### Example

```python
a = [10, 20]
b = a
c = [10, 20]

print(a is b)
print(a is c)

print(a is not c)
```

Output

```text
True
False
True
```

> **Note:** Use `==` to compare values and `is` to compare object identity.

---

# 📌 Membership Operators

## Definition

Membership operators check whether a value exists inside a sequence.

Supported sequence types:

* List
* Tuple
* String
* Set
* Dictionary (checks keys)

---

## Membership Operators Table

| Operator | Description                            | Example              |
| -------- | -------------------------------------- | -------------------- |
| `in`     | Returns `True` if value exists         | `"Python" in text`   |
| `not in` | Returns `True` if value does not exist | `"Java" not in text` |

---

### Example with List

```python
employees = ["Lokesh", "Ganesh", "Charan"]

print("Ganesh" in employees)
print("Naveen" in employees)
```

Output

```text
True
False
```

---

### Example with String

```python
language = "Python"

print("Py" in language)
print("Java" not in language)
```

Output

```text
True
True
```

---

# ⌨️ Input Function

## Definition

The `input()` function is used to accept user input through the terminal.

> **Important:** `input()` always returns a **string (`str`)**.

---

## Syntax

```python
variable_name = input("Enter your name: ")
```

---

## Example

```python
name = input("Enter your name: ")

print(name)
```

Output

```text
Enter your name: Rahul
Rahul
```

---

## Converting Input to Integer

```python
age = int(input("Enter your age: "))

print(age)
```

---

# ✨ f-Strings (Formatted String Literals)

## Definition

An **f-String** is a convenient way to embed variables or expressions inside strings.

---

## Syntax

```python
f"Text {variable_name}"
```

---

## Example

```python
name = "Rahul"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

Output

```text
My name is Rahul and I am 25 years old.
```

---

# 📝 Multi-line Strings

Triple quotes (`'''` or `"""`) create multi-line strings.

```python
message = """
Welcome to Python.

This is a multi-line string.

Thank You.
"""

print(message)
```

---

# 📧 Reusable Email Template

```python
email_template = {
    "subject": "AI Class Scheduled at 8:00 AM",

    "body": """
Dear {student_name},

This is a reminder that the AI class is scheduled on {date} at 8:00 AM.

Please join the session on time and be prepared with your laptop and required materials.

Thank you.

Best Regards,
{sender_name}
"""
}
```

---

## Example Using `.format()`

```python
formatted_email = email_template["body"].format(
    student_name="Rahul",
    date="10 May 2026",
    sender_name="Manideep"
)

print(email_template["subject"])
print(formatted_email)
```

---

## Example Using a Dictionary

```python
student = {
    "student_name": "Rahul",
    "date": "10 May 2026",
    "sender_name": "Manideep"
}

print(email_template["body"].format(**student))
```

---

# 📊 Operator Categories

```text
Operators
│
├── Arithmetic
├── Comparison
├── Logical
├── Assignment
├── Identity
└── Membership
```

---

# 🌟 Best Practices

* Use shorthand assignment operators (`+=`, `-=`, etc.) for cleaner code.
* Use `==` to compare values and `is` only to compare object identity.
* Remember that `input()` always returns a string.
* Prefer f-Strings for readable string formatting.
* Use dictionaries with `.format()` or f-Strings for reusable templates.

---

# 🎤 Frequently Asked Interview Questions

### 1. What are assignment operators?

Assignment operators assign or update the value of a variable.

---

### 2. What is the difference between `=` and `+=`?

| `=`                 | `+=`                                              |
| ------------------- | ------------------------------------------------- |
| Assigns a new value | Adds to the existing value and assigns the result |

---

### 3. What is the difference between `==` and `is`?

| `==`            | `is`                                        |
| --------------- | ------------------------------------------- |
| Compares values | Compares object identity (memory reference) |

---

### 4. What do membership operators do?

Membership operators check whether a value exists in a sequence.

---

### 5. What type does `input()` return?

`input()` always returns a **string (`str`)**.

---

### 6. What is an f-String?

An f-String is a formatted string literal that allows variables and expressions to be embedded directly inside a string.

---

### 7. Why use f-Strings instead of string concatenation?

* Easier to read
* Faster
* Cleaner syntax
* Supports expressions inside `{}`

---

# 🖼️ Reference Diagrams

## Assignment Operators

```text
a = 10
 │
 ├── a += 5  → 15
 ├── a -= 5  → 10
 ├── a *= 2  → 20
 ├── a /= 2  → 10.0
 ├── a %= 3  → 1
 └── a **= 2 → 100
```

---

## Identity Operators

```text
a ─────┐
       │
       ▼
    [10, 20]

b ─────┘

a is b  → True
```

---

## Membership Operators

```text
employees
│
├── Lokesh
├── Ganesh
├── Charan
└── Naveen

"Ganesh" in employees
        │
        ▼
      True
```

---

## Input Function

```text
User
 │
 ▼
input()
 │
 ▼
String Value
 │
 ▼
Variable
```

---

## f-String

```text
Variables
│
├── name = Rahul
└── age = 25

        │
        ▼

f"My name is {name} and I am {age}"

        │
        ▼

"My name is Rahul and I am 25"
```

---

# 📌 Final Summary

* Assignment operators simplify updating variable values.
* Identity operators (`is`, `is not`) compare object identity, while `==` compares values.
* Membership operators (`in`, `not in`) check whether a value exists in a sequence.
* The `input()` function accepts user input and always returns a string.
* f-Strings provide a clean and efficient way to format strings.
* Multi-line strings and reusable templates are useful for emails, reports, and messages.
* These concepts are fundamental in Python and are commonly asked in technical interviews.

### 📖 Suggested Reference Images

![Image](https://images.openai.com/static-rsc-4/rMwTd-FoWbDNHQTSoz_GKP3fasrHIFgjM0gD6fp8hbi3N180zYRFoiyBU8pUII2hz4nF41gwcqZsQ6NzP-12RoJcxI8znYq8mk0V2e3LF3G4dvAkVW4z-xSRhT1chf42Ge43T25O9hdLk2WMKk8_mYXPuVnxVgplYWWbk8DyxxTT2kN1Gxl5xFWKI_5XFwuf?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/LQtKtFicAyXd1CBkaZ6DHIBEO9cTi8jNIpKLD5m1_G3_U8-F0Y27gkZ1e0cCUk1-g8iO07bD4SKptuSjIxH1eH4dcx63C9FzdYEQqU2jOvfZzF3CbalerivfnI76jfq6B97lfp0N2Zvfhbpfy3c6W8CT0QKykHfam7NU_LZ1zL_EMmCNJ08YNPbnBGmyZSBy?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/rvXSyW7UM-8e2OoyAsoOvrmFkCClwqjzDzb_w8JQOMZuGKr75EXZ8utthNj456beUW-MUhCvoOYCC1-AZAmGFgeLJBtEyJ2PvoOyxNs_ixij8tIokfQQEGlxuFvu0y1Ezvw9yg_aRC1LxB81aSlWX28v5VSRbfEG7cSQ0kErcQ1lWtfTtNZuucVz9gWIUgP1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/bbfllL-3epYLWb9o8gLilfgVQ900yAfSLG_QdhLFIjiN0EePTMT79eeJwKI120lA7uOCbwBLyspnqvhP5RwGB87IepSSzyd4mZKt3d_bePLb_YK49Zw9sOcDj73lPXuxfSsDAJKAfs_fxGuQfoncP5ChbOUyS3M_RM5j8Ux171TDw-_Hgu99C4Jmf2WvKGTZ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/fPwsYPHynRdRtRUjgN-Gd66BMJCCOVkGuUDZyDcNPI0lt0DHS2utNURgiDQSRmblgt4AS6YvB5ZxelEFr8gUJfit6nJaLkWcbs4nnY95oTOjWcMqztUEMHIs0jxd-8fgomGmg2KXukalaQDOAFaVkMJY8Ar6BkDmXnhjRQ0Qx1Lsh-X_jGuNxnFmE6ZNZ2mh?purpose=fullsize)
