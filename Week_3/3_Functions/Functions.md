# 🐍 Python Functions – Examples & Mini Projects

> **Complete Interview Guide** covering Function Examples, `return` Statement, Real-World Banking System, Discount Calculator, and Interview Questions.

---

# 📚 Table of Contents

* Function Examples
* Sum Function
* Greeting Function
* Product Function using `return`
* Full Name Constructor
* Mini Project 1 – Banking System
* Mini Project 2 – Discount Calculator
* Best Practices
* Frequently Asked Interview Questions
* Reference Diagrams
* Final Summary

---

# 💻 Example 1 – Calculate Sum

## Program

```python
def calculate_sum(a, b):

    total = a + b

    print("Sum:", total)

calculate_sum(35, 90)
calculate_sum(12, 15)
calculate_sum(45, 90)
```

### Output

```text
Sum: 125
Sum: 27
Sum: 135
```

### Dry Run

| Function Call          | Calculation | Result |
| ---------------------- | ----------- | -----: |
| `calculate_sum(35,90)` | 35 + 90     |    125 |
| `calculate_sum(12,15)` | 12 + 15     |     27 |
| `calculate_sum(45,90)` | 45 + 90     |    135 |

---

# 👋 Example 2 – Greeting Function

## Program

```python
def greet():
    print("Good Morning Folks!")

greet()
greet()
greet()
```

### Output

```text
Good Morning Folks!

Good Morning Folks!

Good Morning Folks!
```

### Explanation

* No parameters.
* Every function call executes the same statement.

---

# ✖ Example 3 – Product using `return`

## Program

```python
def calculate_product(a, b):

    product = a * b

    return product

result = calculate_product(4, 5)

print(result)
```

### Output

```text
20
```

### Dry Run

```text
a = 4
b = 5

product = 20

return 20

result = 20
```

---

# 👤 Example 4 – Construct Full Name

## Program

```python
def construct_fullname(firstname, middlename, lastname):

    fullname = f"{firstname} {middlename} {lastname}".upper()

    print("Fullname:", fullname)

construct_fullname("Aravelli", "Uday", "Kiran")
construct_fullname("David", "", "Warner")
construct_fullname("Keerthi", "", "P")
```

### Output

```text
Fullname: ARAVELLI UDAY KIRAN

Fullname: DAVID WARNER

Fullname: KEERTHI P
```

### Explanation

### f-string

```python
f"{firstname} {middlename} {lastname}"
```

Used to insert variable values into a string.

### `.upper()`

```python
.upper()
```

Converts the complete string to uppercase.

---

# 🏦 Mini Project 1 – Banking System

## Requirement

Create functions to:

* Check Balance
* Withdraw Money

---

## Program

```python
def check_balance(balance):
    print(f"Your current balance is {balance}")

def withdraw(balance, amount):

    if amount <= balance:
        balance -= amount
        print(f"Withdrawal is successful, new balance is {balance}")
        return balance
    else:
        print("Insufficient balance")
        return balance
```

---

## Check Balance

```python
account_balance = 5000

check_balance(account_balance)
```

### Output

```text
Your current balance is 5000
```

---

## Withdrawal Example 1

```python
account_balance = 5000

check_balance(account_balance)

account_balance = withdraw(account_balance, 2000)
```

### Output

```text
Your current balance is 5000

Withdrawal is successful, new balance is 3000
```

---

### Dry Run

| Step            | Balance |
| --------------- | ------: |
| Initial Balance |    5000 |
| Withdraw 2000   |    3000 |

---

## Withdrawal Example 2

```python
account_balance = withdraw(account_balance, 4050)
```

### Output

```text
Insufficient balance
```

> If the balance were still **5000**, the new balance would become **950**.

---

## Updating Balance After Every Withdrawal

```python
account_balance = 5000

check_balance(account_balance)

account_balance = withdraw(account_balance, 2000)

account_balance = withdraw(account_balance, 200)

account_balance = withdraw(account_balance, 450)
```

### Output

```text
Your current balance is 5000

Withdrawal is successful, new balance is 3000

Withdrawal is successful, new balance is 2800

Withdrawal is successful, new balance is 2350
```

---

### Dry Run

| Transaction   | Balance |
| ------------- | ------: |
| Initial       |    5000 |
| Withdraw 2000 |    3000 |
| Withdraw 200  |    2800 |
| Withdraw 450  |    2350 |

---

# 💰 Mini Project 2 – Discount Calculator

## Requirement

Calculate the final payable amount based on the purchase amount.

---

## Discount Rules

| Purchase Amount |    Discount |
| --------------: | ----------: |
| ₹5000 and above |         20% |
| ₹3000 and above |         10% |
| ₹1000 and above |          5% |
|     Below ₹1000 | No Discount |

---

## Program

```python
def calculate_discounted_amount(total_amount):

    if total_amount >= 5000:
        return total_amount - (total_amount * 0.20)

    elif total_amount >= 3000:
        return total_amount - (total_amount * 0.10)

    elif total_amount >= 1000:
        return total_amount - (total_amount * 0.05)

    else:
        return total_amount
```

---

## Example 1

```python
discounted_amount = calculate_discounted_amount(50000)

print(discounted_amount)
```

### Output

```text
40000.0
```

### Dry Run

| Purchase Amount | Discount | Final Amount |
| --------------: | -------: | -----------: |
|           50000 |      20% |        40000 |

---

## Example 2

```python
discounted_amount = calculate_discounted_amount(4890)

print(discounted_amount)
```

### Output

```text
4401.0
```

### Dry Run

| Purchase Amount | Discount | Final Amount |
| --------------: | -------: | -----------: |
|            4890 |      10% |         4401 |

---

# 🌟 Best Practices

* Write one function for one specific task.
* Use descriptive function names.
* Return values instead of only printing them.
* Reuse functions wherever possible.
* Store returned values for future operations.
* Avoid duplicate code.
* Follow Python's 4-space indentation.

---

# 🎤 Frequently Asked Interview Questions

### 1. Why do we use functions?

* Reduce code duplication.
* Improve reusability.
* Make programs modular and maintainable.

---

### 2. What is the difference between `print()` and `return`?

| `print()`              | `return`                       |
| ---------------------- | ------------------------------ |
| Displays output        | Sends value back to the caller |
| Cannot be reused later | Can be stored and reused       |

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

---

### 3. Why should we store the returned value?

```python
balance = withdraw(balance, 2000)
```

The updated balance is saved, so future transactions use the latest balance.

---

### 4. Why is `return` preferred in reusable functions?

Because the returned value can be used in calculations, conditions, or passed to other functions.

---

# 📊 Reference Diagrams

## Function Execution

```text
Define Function
      │
      ▼
Call Function
      │
      ▼
Execute Code
      │
      ▼
Return Result
      │
      ▼
Continue Program
```

---

## Banking System Flow

```text
Start
  │
  ▼
Check Balance
  │
  ▼
Enter Withdrawal Amount
  │
  ▼
Amount <= Balance?
  │
 ┌┴───────────┐
 │            │
Yes          No
 │            │
 ▼            ▼
Deduct     Insufficient Balance
 │
 ▼
Return New Balance
```

---

## Discount Calculator Flow

```text
Purchase Amount
       │
       ▼
>= 5000 ?
 │
 ├── Yes → 20%
 │
 └── No
      │
      ▼
>= 3000 ?
 │
 ├── Yes → 10%
 │
 └── No
      │
      ▼
>= 1000 ?
 │
 ├── Yes → 5%
 │
 └── No → No Discount
```

---

# 📌 Final Summary

| Concept             | Purpose                                 |
| ------------------- | --------------------------------------- |
| Function            | Reusable block of code                  |
| Parameters          | Receive values                          |
| Arguments           | Pass values                             |
| `return`            | Send value back to caller               |
| Banking System      | Demonstrates reusable business logic    |
| Discount Calculator | Uses conditional logic inside functions |

## ✅ Key Takeaways

* Functions eliminate repetitive code.
* Use `return` when a value needs to be reused.
* Store returned values to maintain updated data.
* Functions help build real-world applications such as banking systems, billing software, and discount calculators.
* Writing small, reusable functions improves code quality and maintainability.
* Function-based programming is a core Python skill and a common interview topic.
