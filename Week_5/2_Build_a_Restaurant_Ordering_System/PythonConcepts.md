Here are simple, interview-friendly definitions and explanations for each concept used in your **Restaurant Ordering System**.

---

# 🧩 Python Concepts Used in the Restaurant Ordering System

---

# 1️⃣ Functions

## 📖 Definition

A **function** is a reusable block of code that performs a specific task. It helps avoid writing the same code multiple times.

## 📝 Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

## 💻 Example

```python
def greet():
    print("Welcome!")

greet()
```

## 🧠 Why Used in This Project?

Functions divide the program into smaller tasks.

* `display_menu()` → Displays the menu.
* `take_order()` → Takes customer orders.
* `calculate_bill()` → Calculates the bill.
* `print_bill()` → Prints the final bill.

## 🌍 Real-World Example

ATM Machine

* Check Balance
* Withdraw Money
* Deposit Money

Each operation is a separate function.

---

# 2️⃣ Dictionary

## 📖 Definition

A **dictionary** is a collection of **key-value pairs** used to store related information.

## 📝 Syntax

```python
dictionary = {
    "key": value
}
```

## 💻 Example

```python
student = {
    "name": "Ramesh",
    "age": 22
}

print(student["name"])
```

## 🧠 Why Used in This Project?

The menu is stored as a dictionary because:

* Food name → Key
* Price → Value

Example:

```python
menu = {
    "Pizza": 400,
    "Burger": 300
}
```

Finding the price is very fast:

```python
menu["Pizza"]
```

Output

```text
400
```

---

# 3️⃣ Loops (for, while)

## 📖 Definition

A **loop** repeatedly executes a block of code until a condition is met.

### Types

* `for` loop
* `while` loop

---

## 📝 for Loop Syntax

```python
for item in sequence:
    statements
```

### Example

```python
colors = ["Red", "Blue", "Green"]

for color in colors:
    print(color)
```

---

## 📝 while Loop Syntax

```python
while condition:
    statements
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## 🧠 Why Used in This Project?

### for Loop

Used to display:

* Menu items
* Ordered items
* Bill details

Example

```python
for item, price in menu.items():
    print(item, price)
```

---

### while Loop

Used because the customer can order **any number of items**.

```python
while item != "done":
```

The loop stops only when the customer enters:

```text
done
```

---

# 4️⃣ Conditional Statements (if, else)

## 📖 Definition

Conditional statements execute different blocks of code based on a condition.

## 📝 Syntax

```python
if condition:
    statements
else:
    statements
```

## 💻 Example

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

## 🧠 Why Used in This Project?

To check:

* Whether an item exists in the menu.
* Whether the customer gets a discount.

Example

```python
if item in menu:
```

Example

```python
if total_amount > 1000:
```

---

# 5️⃣ User Input (input())

## 📖 Definition

The `input()` function accepts input from the keyboard.

**Note:** `input()` always returns a string.

## 📝 Syntax

```python
value = input("Enter value: ")
```

## 💻 Example

```python
name = input("Enter your name: ")

print(name)
```

## 🧠 Why Used in This Project?

To allow the customer to:

* Enter food items
* Enter quantities

Example

```python
item = input("Enter item: ")
```

---

# 6️⃣ Ternary Operator

## 📖 Definition

A **Ternary Operator** is a one-line shortcut for an `if-else` statement.

## 📝 Syntax

```python
value_if_true if condition else value_if_false
```

## 💻 Example

```python
status = "Adult" if age >= 18 else "Minor"
```

## 🧠 Why Used in This Project?

To calculate the discount.

```python
discount = total_amount * 0.10 if total_amount > 1000 else 0
```

Instead of

```python
if total_amount > 1000:
    discount = total_amount * 0.10
else:
    discount = 0
```

---

# 7️⃣ return Statement

## 📖 Definition

The `return` statement sends a value back from a function to the caller.

## 📝 Syntax

```python
return value
```

## 💻 Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```text
30
```

## 🧠 Why Used in This Project?

To return:

* Customer order
* Total amount
* Discount

Example

```python
return order
```

Example

```python
return total_amount, discount
```

---

# 8️⃣ Dictionary `get()` Method

## 📖 Definition

The `get()` method retrieves the value of a key. If the key does not exist, it returns a default value instead of causing an error.

## 📝 Syntax

```python
dictionary.get(key, default_value)
```

## 💻 Example

```python
student = {
    "name": "Ramesh"
}

print(student.get("name"))
print(student.get("age", 0))
```

Output

```text
Ramesh
0
```

## 🧠 Why Used in This Project?

The customer may order the same item multiple times.

Instead of replacing the old quantity, we add it.

```python
order[item] = order.get(item, 0) + quantity
```

### Dry Run

Initially

```python
order = {}
```

Customer orders

```text
Pizza
```

Quantity

```text
2
```

Result

```python
{
    "Pizza": 2
}
```

Customer orders Pizza again

Quantity

```text
1
```

`order.get("Pizza", 0)` returns `2`

New quantity

```text
2 + 1 = 3
```

Final dictionary

```python
{
    "Pizza": 3
}
```

Without `get()`, trying to access a missing key would raise a `KeyError`.

---

# 📋 Final Summary

| Concept                | Purpose in This Project                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Functions**          | Divide the program into reusable tasks like displaying the menu, taking orders, calculating bills, and printing the bill. |
| **Dictionary**         | Store menu items as key-value pairs (item → price) for fast lookup.                                                       |
| **for Loop**           | Display menu items and generate the final bill.                                                                           |
| **while Loop**         | Allow customers to order multiple items until they enter `"done"`.                                                        |
| **if-else**            | Check item availability and determine discount eligibility.                                                               |
| **input()**            | Accept item names and quantities from the customer.                                                                       |
| **Ternary Operator**   | Apply a 10% discount in a concise one-line expression.                                                                    |
| **return**             | Send calculated data (orders, totals, discounts) back to the calling code.                                                |
| **Dictionary `get()`** | Safely retrieve existing quantities and update repeated orders without errors.                                            |
