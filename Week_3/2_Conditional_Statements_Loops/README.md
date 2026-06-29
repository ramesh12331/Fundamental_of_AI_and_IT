Your README-style notes are a standalone document, so here's a polished version in the same format.

# 🐍 Python Conditional Statements & Loops – Complete Interview Notes

> A beginner-friendly guide covering Conditional Statements, Ternary Operator, For Loop, While Loop, Practice Programs, Interview Questions, and Summary.

---

# 📚 Table of Contents

* Introduction
* Conditional Statements
* Types of Conditional Statements
* `if` Statement
* `if-else` Statement
* `if-elif-else` Statement
* Practice Tasks
* Ternary Operator
* Looping Statements
* `for` Loop
* `range()` Function
* `while` Loop
* Difference Between `for` and `while`
* Best Practices
* Frequently Asked Interview Questions
* Final Summary

---

# 🐍 Introduction

Conditional statements allow a program to make decisions based on conditions.

Loops allow a program to execute the same block of code multiple times without writing duplicate code.

---

# 🔀 Conditional Statements

## Definition

Conditional statements execute different blocks of code depending on whether a condition is **True** or **False**.

---

## Rules

* Every conditional statement ends with a colon (`:`).
* The block inside the condition must be indented.
* Python recommends **4 spaces** for indentation (PEP 8).

### Basic Syntax

```python
if condition:
    statement
```

---

# 📖 Types of Conditional Statements

1. `if`
2. `if-else`
3. `if-elif-else`

---

# 1️⃣ if Statement

Executes a block of code only when the condition is **True**.

### Syntax

```python
if condition:
    statement1
    statement2
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

### Output

```text
Eligible to Vote
```

---

# 2️⃣ if-else Statement

Executes one block if the condition is **True**, otherwise executes another block.

### Syntax

```python
if condition:
    statements
else:
    statements
```

### Example

```python
num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

### Output

```text
Odd Number
```

---

# 3️⃣ if-elif-else Statement

Used when multiple conditions need to be checked.

### Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")
```

### Output

```text
Grade B
```

---

# 💻 Practice Task 1 – Student Grade Calculator

### Requirement

Assign grades based on marks.

| Marks    | Grade |
| -------- | ----- |
| 90–100   | A     |
| 75–89    | B     |
| 60–74    | C     |
| 40–59    | D     |
| Below 40 | Fail  |

### Solution

```python
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")
```

---

# 🛒 Practice Task 2 – Online Shopping Discount

### Requirement

| Cart Amount   | Discount |
| ------------- | -------- |
| Above ₹10,000 | 20%      |
| Above ₹5,000  | 10%      |
| Above ₹2,000  | 5%       |

**Extra Rule**

Premium users receive an additional **5% discount**.

### Solution

```python
amount = float(input("Enter Cart Amount: "))
premium = input("Premium User (yes/no): ").lower()

discount = 0

if amount > 10000:
    discount = 20
elif amount > 5000:
    discount = 10
elif amount > 2000:
    discount = 5

if premium == "yes":
    discount += 5

print(f"Total Discount: {discount}%")
```

---

# ⚡ Ternary Operator (Conditional Expression)

The ternary operator is a shorter way of writing a simple `if-else` statement.

### Syntax

```python
variable = value_if_true if condition else value_if_false
```

### Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

### Output

```text
Adult
```

---

## Equivalent if-else

```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)
```

---

# 🔁 Looping Statements

## Definition

Loops execute a block of code repeatedly until a condition changes or all items are processed.

### Types of Loops

* `for` loop
* `while` loop

---

# 1️⃣ for Loop

The `for` loop iterates over a sequence such as a list, tuple, string, or `range()`.

### Syntax

```python
for variable in sequence:
    statements
```

---

## Using `range()`

```python
range(0, 5)
```

Produces:

```text
0 1 2 3 4
```

> The ending value (`5`) is **not included**.

---

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

## Print Even Numbers

```python
for i in range(2, 11, 2):
    print(i)
```

### Output

```text
2
4
6
8
10
```

---

## Print Table of 5

```python
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
```

---

## Iterate Through a List

```python
employees = ["Lokesh", "Ganesh", "Charan"]

for employee in employees:
    print(employee)
```

---

# 2️⃣ while Loop

A `while` loop executes as long as its condition remains **True**.

### Syntax

```python
while condition:
    statements
```

---

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

---

## Countdown Example

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Done!")
```

---

# 📊 Difference Between `for` and `while`

| for Loop                                    | while Loop                                    |
| ------------------------------------------- | --------------------------------------------- |
| Used when the number of iterations is known | Used when the number of iterations is unknown |
| Iterates over a sequence                    | Runs until the condition becomes False        |
| Simpler for fixed repetitions               | Better for condition-based repetition         |
| Uses `range()` or iterables                 | Uses Boolean conditions                       |

---

# 🌟 Best Practices

* Use meaningful variable names.
* Keep conditions simple and readable.
* Prefer `for` loops when iterating over sequences.
* Use `while` loops when repetition depends on a condition.
* Avoid infinite loops unless intentionally required.
* Maintain consistent indentation (4 spaces).

---

# 🎤 Frequently Asked Interview Questions

### 1. What is a conditional statement?

A statement that executes different blocks of code depending on whether a condition is **True** or **False**.

---

### 2. What are the types of conditional statements?

* `if`
* `if-else`
* `if-elif-else`

---

### 3. What is the ternary operator?

A one-line shorthand for a simple `if-else` statement.

---

### 4. What is the difference between `if` and `if-else`?

| if                                       | if-else                                           |
| ---------------------------------------- | ------------------------------------------------- |
| Executes only when the condition is True | Executes one block for True and another for False |

---

### 5. What is a loop?

A loop repeatedly executes a block of code.

---

### 6. What is the difference between `for` and `while`?

A `for` loop is best for known iterations, while a `while` loop is best when the number of iterations depends on a condition.

---

### 7. What does `range(5)` return?

It generates the sequence:

```text
0, 1, 2, 3, 4
```

---

# 🖼 Reference Diagrams

## Conditional Flow

```text
Condition
    │
    ▼
 True? ─────── No
   │             │
   ▼             ▼
Execute      Else Block
   │
   ▼
Continue Program
```

---

## if-elif-else Flow

```text
Condition 1?
   │
True ─► Block 1
   │
False
   │
Condition 2?
   │
True ─► Block 2
   │
False
   │
Else Block
```

---

## for Loop Flow

```text
Start
  │
  ▼
Sequence
  │
  ▼
Next Item
  │
  ▼
Execute Block
  │
  ▼
More Items?
 │       │
Yes      No
 │        ▼
 └────► End
```

---

## while Loop Flow

```text
Condition
   │
True?
 │    │
Yes   No
 │     ▼
 ▼    End
Execute
 │
 ▼
Update Condition
 │
 └───────────────►
```

---

# 📌 Final Summary

| Concept          | Purpose                               |
| ---------------- | ------------------------------------- |
| `if`             | Execute code when a condition is True |
| `if-else`        | Choose between two code blocks        |
| `if-elif-else`   | Handle multiple conditions            |
| Ternary Operator | Write simple `if-else` in one line    |
| `for` Loop       | Iterate over a sequence               |
| `range()`        | Generate a sequence of numbers        |
| `while` Loop     | Repeat code while a condition is True |

### Key Takeaways

* Conditional statements help programs make decisions.
* The ternary operator simplifies simple `if-else` expressions.
* `for` loops are ideal when the number of iterations is known.
* `while` loops are useful when repetition depends on a condition.
* These concepts are fundamental to Python programming and are frequently asked in coding interviews.

For better visual understanding, you can include these reference images in your README:

![Image](https://images.openai.com/static-rsc-4/r919zl7b0GWmATpamsq6FidicU4RXDVTg7aCqf8CLCkPGDKnU9NQifrjOIMUPLInaocuemyLfIV1KSHTA1uVS4J4lr4CSiVDS5s_vI9SxrDtY0kqHTbP7BmQVkM6tq-3bXuoHgKfOYSA4Q2iDJvIv9Lc7a-EIEkxweBy2iY6v48DmZttCpuN5zNVNPbxEcsk?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/1ADQZOhy1B3IF9cLKoMIxY10xJ0ZfgVCuiWk5l8MAynOjucnSjGn0tlQhc-U-4TmxNCakeSNSMZf-zpmZLLC-4Qw96CMJq9RzGSBCUICazYihuwXeiEEGaOLkesjTLwKh17O19eJqgJbnTfJ1lEkAQPNSjcGy-cJtsOW3CZ2Q3w4PN1XMj_MhwTCN94M8RE5?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pOm5ECoCpKnfQVXKbUefN6y0K9PzTp5vWL_CBkQz2-7ZHaC7-sF7d4jb9OcSxAsFOI4AKcEl1ySrCTMh2jB0W6P-3TRYYAr79HhFNSl30x3TVKY1wSxS4O0lecNBt5AgpWSa814WH362Le1i5F7kFqvwfjNH0Ji4ssvDxPz3r7bZ7T7Aq50IDOrmV334OA1o?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/bhNUxU1nX2wl-0bfJZKLTv108cC2oKGsgLsM22hJQWgPEz_WfBCH3KHveikdpJHCCh3CAWIeey_Q75L511Zwuew0kBq19ONFbsQsAEa5DmE43jlhSYG_5n0pciWgsu9ZVQusTBpiyLFaNEYF11poKtGL4EzJFOkQfUu4KNjKbYHgp-PDT1GWfb_y3FzSX2fw?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/3iN-NW8lj0RxsuHXuDtw0mi4cgPu65XS7EAEShe1wKFyDbsRe_5wUAZerHpScXdMz9b5h5eQ88VrRCfv-o4dhtMQv8vpfASirtio4Ap7bE1NAuelWLjIeUctA8Ah1AZNEvNlWf7oqAnIDKhwsmRhZ3Y-5rRJbzSNxO5z1s7RHaIyJpL42qC_fh5Iar0Gsp6Y?purpose=fullsize)
