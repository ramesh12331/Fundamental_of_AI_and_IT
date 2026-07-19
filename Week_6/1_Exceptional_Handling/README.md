Yes! Using icons makes your notes much more attractive and easier to revise. Here's a clean icon style you can use consistently for all your Python notes.

---

# 🛡️ 📘 Python Exception Handling

---

# 📖 What is Exception Handling?

## 📌 Definition

**Exception Handling** allows us to handle runtime errors, ensuring that the program doesn't crash unexpectedly.

---

# ❓ What is an Exception?

## 📌 Definition

An **Exception** is an error that occurs during the execution (runtime) of a program.

---

# ⚠️ Common Exceptions

| 🚨 Exception         | 📝 Description                     |
| -------------------- | ---------------------------------- |
| ➗ ZeroDivisionError  | Division by zero                   |
| 🔢 ValueError        | Invalid value passed to a function |
| 🔑 KeyError          | Dictionary key not found           |
| 📋 IndexError        | List index out of range            |
| 🔤 TypeError         | Invalid data type                  |
| 📂 FileNotFoundError | File not found                     |

---

# ⚙️ Exception Handling

## 📝 Syntax

```python
try:
    # Code that may cause an exception

except ExceptionType:
    # Code to handle the exception
```

---

# 💻 Example 1: ZeroDivisionError

```python
try:
    num1 = 10
    num2 = 0
    print(num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### 🖥️ Output

```text
Cannot divide by zero.
```

---

# 💻 Example 2: ValueError

```python
try:
    age = int(input("Enter Age: "))
    print(age)

except ValueError:
    print("Please enter a valid number.")
```

---

# 💻 Example 3: IndexError

```python
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist.")
```

---

# 💻 Example 4: KeyError

```python
student = {
    "name": "Ramesh",
    "age": 24
}

try:
    print(student["city"])

except KeyError:
    print("Key not found.")
```

---

# 🔄 finally Block

## 📌 Definition

The **finally** block is always executed whether an exception occurs or not.

It is commonly used for cleanup operations like:

* 📂 Closing files
* 🗄️ Closing database connections
* 🌐 Releasing network resources

---

## 📝 Syntax

```python
try:
    # Code

except ExceptionType:
    # Handle Exception

finally:
    # Always Executes
```

---

## 💻 Example

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero.")

finally:
    print("Program Finished.")
```

### 🖥️ Output

```text
Division by zero.
Program Finished.
```

---

# 💻 Example from Class

```python
company_name = "Data Valley"

print(company_name[5:14])
```

### 🖥️ Output

```text
Valley
```

---

# 🛠️ Custom Exception

## 📌 Definition

A **Custom Exception** is an exception created by the programmer to handle application-specific errors.

---

## 📝 Syntax

```python
class CustomException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

---

## 💻 Example

```python
class OutOfStockError(Exception):

    def __init__(self, message):
        super().__init__(message)


stock = 5
quantity = 8

try:
    if quantity > stock:
        raise OutOfStockError("Product is out of stock.")

except OutOfStockError as error:
    print(error)
```

### 🖥️ Output

```text
Product is out of stock.
```

---

# 🛒 E-Commerce Order System

## 📋 Problem Statement

Build a simple console-based checkout system where a user:

* 🛍️ Selects a product.
* 🔢 Enters quantity.
* 🎟️ Applies a coupon (optional).
* 💰 Gets the final bill.

### ⚠️ Handle the Following Exceptions

* 🔑 Invalid product selection → **KeyError**
* 📦 Out-of-stock quantity → **Custom OutOfStockError**
* 🎟️ Invalid coupon code → **KeyError**
* ✅ Always display order confirmation using **finally**

---

## 💻 Complete Solution

```python
class OutOfStockError(Exception):
    def __init__(self, message):
        super().__init__(message)


products = {
    "Laptop": {"price": 60000, "stock": 5},
    "Mouse": {"price": 500, "stock": 20},
    "Keyboard": {"price": 1000, "stock": 10}
}

coupons = {
    "SAVE10": 10,
    "SAVE20": 20
}

try:
    product = input("Enter Product: ")

    if product not in products:
        raise KeyError("Invalid Product")

    quantity = int(input("Enter Quantity: "))

    if quantity > products[product]["stock"]:
        raise OutOfStockError("Product Out of Stock")

    total = quantity * products[product]["price"]

    coupon = input("Enter Coupon Code (Press Enter to Skip): ")

    if coupon:

        if coupon not in coupons:
            raise KeyError("Invalid Coupon Code")

        discount = coupons[coupon]
        total = total - (total * discount / 100)

    print("Final Bill =", total)

except KeyError as error:
    print(error)

except OutOfStockError as error:
    print(error)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Order Process Completed.")
```

---

# 📝 Final Summary

✅ **Exception** → Runtime error that occurs while executing a program.

✅ **Exception Handling** → Prevents the program from crashing by handling runtime errors.

✅ **try** → Contains code that may raise an exception.

✅ **except** → Catches and handles the exception.

✅ **finally** → Always executes whether an exception occurs or not.

✅ **raise** → Used to manually raise an exception.

✅ **Custom Exception** → User-defined exception created by inheriting from the `Exception` class.

### 🚨 Common Exceptions

* ➗ ZeroDivisionError
* 🔢 ValueError
* 📋 IndexError
* 🔑 KeyError
* 🔤 TypeError
* 📂 FileNotFoundError

---

# 🎤 Interview Questions

### ❓ 1. What is Exception Handling?

**Answer:**

Exception Handling is a mechanism used to handle runtime errors without stopping the execution of a program.

---

### ❓ 2. What is an Exception?

**Answer:**

An exception is an error that occurs during program execution.

---

### ❓ 3. Name some common exceptions.

* ➗ ZeroDivisionError
* 🔢 ValueError
* 🔑 KeyError
* 📋 IndexError
* 🔤 TypeError
* 📂 FileNotFoundError

---

### ❓ 4. What is the purpose of the `try` block?

**Answer:**

The `try` block contains code that may raise an exception.

---

### ❓ 5. What is the purpose of the `except` block?

**Answer:**

The `except` block catches and handles exceptions raised in the `try` block.

---

### ❓ 6. What is the purpose of the `finally` block?

**Answer:**

The `finally` block always executes whether an exception occurs or not. It is commonly used for cleanup tasks like closing files or database connections.

---

### ❓ 7. What is a Custom Exception?

**Answer:**

A Custom Exception is a user-defined exception created by inheriting from Python's built-in `Exception` class.

---

