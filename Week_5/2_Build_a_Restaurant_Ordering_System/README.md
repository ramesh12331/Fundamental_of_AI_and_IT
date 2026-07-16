# 🍽️ Mini Project: Restaurant Ordering System

---

# 🎯 Introduction

A **Restaurant Ordering System** is a simple Python application that allows customers to:

* 📋 View the restaurant menu
* 🍕 Order multiple food items
* 🔢 Enter the quantity of each item
* 💰 Calculate the total bill
* 🎁 Apply a **10% discount** if the total bill is more than **₹1000**
* 🧾 Print the final bill

This project demonstrates the practical use of **functions**, **dictionaries**, **loops**, **conditional statements**, and **user input**.

---

# 📖 Problem Statement

Create a restaurant ordering system that can:

* Display the menu with prices.
* Allow customers to order multiple items.
* Calculate the total bill.
* Apply a **10% discount** if the bill exceeds **₹1000**.
* Display a detailed bill.

---

# 🧠 Problem Analysis

Before writing the code, analyze the problem.

### Inputs

* Menu (Dictionary)
* Item name
* Quantity

### Processing

* Display menu
* Take customer orders
* Calculate total
* Check discount eligibility
* Generate bill

### Outputs

* Ordered items
* Discount
* Final payable amount

---

# 📊 Flow Diagram

```text
              Start
                 │
                 ▼
         Create Menu Dictionary
                 │
                 ▼
          Display Menu
                 │
                 ▼
      Take Customer Order
                 │
                 ▼
   Is Item Available in Menu?
         │              │
       Yes             No
        │               │
        ▼               ▼
 Ask Quantity      Show Error
        │               │
        └──────┬────────┘
               ▼
      Customer Finished?
          │          │
         No         Yes
          │          ▼
          └────► Calculate Bill
                    │
                    ▼
      Total > ₹1000 ?
         │            │
       Yes            No
        │              │
 Apply 10% Discount   No Discount
        │
        ▼
      Print Bill
        │
        ▼
        End
```

---

# 🗂 Program Structure

| Function         | Purpose                              |
| ---------------- | ------------------------------------ |
| display_menu()   | Displays all menu items              |
| take_order()     | Accepts customer orders              |
| calculate_bill() | Calculates total amount and discount |
| print_bill()     | Prints the final bill                |

---

# 🍽 Menu Dictionary

```python
menu = {
    'Four Cheese Pizza': 400,
    'BBQ Bacon Burger': 319,
    'Lasagna': 340,
    'Onion Rings': 140,
    'Minestrone Soup': 145,
    'Caesar Salad': 199,
    'Coca Cola': 60,
    'Fresh Lime Soda': 80,
    'Mango Lassi': 120,
    'Chocolate Brownie': 180,
    'Cheesecake': 220,
}
```

---

# 1️⃣ display_menu()

## 📖 Definition

Displays all food items and their prices.

---

## 📝 Syntax

```python
display_menu(menu)
```

---

## 💻 Code

```python
def display_menu(menu):
    print("-"*25)
    print("Menu")
    print("-"*25)

    for item, price in menu.items():
        print(f"{item} : {price}")
```

---

## 🧠 Logic Behind the Code

### Step 1

Receive the menu dictionary.

↓

### Step 2

Print the heading.

↓

### Step 3

Loop through each item.

↓

### Step 4

Display item name and price.

---

## 🔍 Dry Run

```text
Pizza → 400

Burger → 319

Lasagna → 340
```

---

# 2️⃣ take_order()

## 📖 Definition

Allows the customer to order multiple items.

---

## 📝 Syntax

```python
order = take_order(menu)
```

---

## 💻 Code

```python
def take_order(menu):

    order = {}

    item = input("Enter item (or done): ")

    while item != "done":

        if item in menu:

            quantity = int(input("Quantity: "))

            order[item] = order.get(item, 0) + quantity

        else:

            print("Item not available")

        item = input("Enter item (or done): ")

    return order
```

---

## 🧠 Logic Behind the Code

### Step 1

Create an empty dictionary.

↓

### Step 2

Ask customer for an item.

↓

### Step 3

Check whether item exists.

↓

### Step 4

If available

Ask quantity.

↓

### Step 5

Store quantity.

↓

### Step 6

Repeat until customer enters

```text
done
```

---

## 🔍 Dry Run

Customer enters

```text
Pizza
```

↓

Quantity

```text
2
```

Dictionary becomes

```python
{
"Pizza":2
}
```

Customer enters

```text
Burger
```

↓

Quantity

```text
1
```

Dictionary becomes

```python
{
"Pizza":2,
"Burger":1
}
```

Customer enters

```text
done
```

Loop stops.

---

# Why use

```python
order.get(item,0)
```

Suppose customer orders Pizza twice.

First

```python
Pizza = 2
```

Later

```python
Pizza = 1
```

Instead of replacing,

```python
2 + 1 = 3
```

---

# 3️⃣ calculate_bill()

## 📖 Definition

Calculates total bill and applies discount.

---

## 📝 Syntax

```python
total_amount, discount = calculate_bill(menu, order)
```

---

## 💻 Code

```python
def calculate_bill(menu, order):

    total_amount = 0

    for item, quantity in order.items():

        item_cost = menu[item] * quantity

        total_amount += item_cost

    discount = total_amount * 0.10 if total_amount > 1000 else 0

    return total_amount, discount
```

---

## 🧠 Logic Behind the Code

Step 1

Start total amount with

```text
0
```

↓

Step 2

Loop through every ordered item.

↓

Step 3

Calculate

```text
Price × Quantity
```

↓

Step 4

Add to total.

↓

Step 5

Check

```text
Total > 1000 ?
```

↓

If yes

Apply

```text
10%
```

Otherwise

```text
0
```

---

## 🔍 Dry Run

Order

```text
Pizza ×2

400 ×2 =800

Burger ×1

319 ×1 =319
```

Total

```text
1119
```

Discount

```text
111.9
```

Final

```text
1007.1
```

---

# Why use Ternary Operator?

Instead of

```python
if total_amount > 1000:
    discount = total_amount * 0.10
else:
    discount = 0
```

we write

```python
discount = total_amount * 0.10 if total_amount > 1000 else 0
```

Short and clean.

---

# 4️⃣ print_bill()

## 📖 Definition

Prints the customer bill.

---

## 📝 Syntax

```python
print_bill(menu, order, total_amount, discount)
```

---

## 💻 Code

```python
def print_bill(menu, order, total_amount, discount):

    print("Bill")

    print("-"*20)

    for item, quantity in order.items():

        print(f"{item} * {quantity} = {menu[item]*quantity}")

    if discount:

        print(f"Discount : {discount}")

    print(f"Final Amount : {total_amount-discount}")
```

---

## 🧠 Logic Behind the Code

Step 1

Print heading.

↓

Step 2

Loop through ordered items.

↓

Step 3

Print

```text
Item × Quantity = Price
```

↓

Step 4

Print discount (if applicable).

↓

Step 5

Print final amount.

---

## 🖥 Sample Output

```text
-------------------------
Menu
-------------------------

Four Cheese Pizza : 400
BBQ Bacon Burger : 319
Lasagna : 340
...

Enter item : Four Cheese Pizza

Quantity : 2

Enter item : BBQ Bacon Burger

Quantity : 1

Enter item : done

Bill

--------------------

Four Cheese Pizza * 2 = 800

BBQ Bacon Burger * 1 = 319

Discount Applied : 111.9

Final Amount : 1007.1
```

---

# 🌍 Real-world Applications

* 🍽 Restaurant Billing System
* 🛒 Online Food Ordering Apps
* 🍕 Domino's Ordering System
* 🍔 Swiggy
* 🛵 Zomato
* ☕ Cafe Billing Software

---

# 💡 Best Practices

* ✔ Divide the program into functions.
* ✔ Use dictionaries for menu data.
* ✔ Validate user input.
* ✔ Use meaningful variable names.
* ✔ Return values instead of relying only on `print()`.
* ✔ Keep each function focused on one task.

---

# 🎤 Interview Questions & Answers

### 1. Why is a dictionary used for the menu?

**Answer:** A dictionary stores food items as keys and prices as values, making price lookup fast and simple.

---

### 2. Why do we use functions?

**Answer:** Functions reduce code duplication and make programs modular, reusable, and easier to maintain.

---

### 3. What does `order.get(item, 0)` do?

**Answer:** It returns the current quantity of the item. If the item is not present, it returns `0`, preventing a `KeyError`.

---

### 4. Why do we return `total_amount` and `discount`?

**Answer:** Returning values allows other parts of the program to use the calculated results.

---

### 5. Why use a `while` loop in `take_order()`?

**Answer:** Because the number of items the customer wants to order is unknown in advance.

---

### 6. Which Python concepts are used in this project?

**Answer:**

* Functions
* Dictionary
* Loops (`for`, `while`)
* Conditional Statements (`if`, `else`)
* User Input (`input()`)
* Ternary Operator
* `return`
* `get()` Dictionary Method

---

# 📌 Key Points to Remember

* ✅ Functions make code reusable.
* ✅ Dictionaries store menu items efficiently.
* ✅ `while` loops are useful when the number of iterations is unknown.
* ✅ `for` loops process ordered items one by one.
* ✅ `get()` safely retrieves dictionary values.
* ✅ Ternary operators simplify simple `if-else` logic.
* ✅ Returning values makes functions reusable.

---

# 📋 Final Summary

| Concept            | Purpose                                   |
| ------------------ | ----------------------------------------- |
| `display_menu()`   | Display all food items and prices         |
| `take_order()`     | Collect customer orders                   |
| `order.get()`      | Handle repeated item orders safely        |
| `calculate_bill()` | Compute total amount and discount         |
| Ternary Operator   | Apply discount in one line                |
| `print_bill()`     | Display detailed bill                     |
| Dictionary         | Store menu and order information          |
| `for` Loop         | Process menu and ordered items            |
| `while` Loop       | Accept multiple orders until `done`       |
| Functions          | Organize the program into reusable blocks |

This project is an excellent beginner-level mini project that combines dictionaries, functions, loops, user input, conditional logic, and billing calculations in a real-world scenario.
