This is an excellent introduction to **Python OOP (Classes, Objects, Constructor, Methods, Encapsulation)**. For your GitHub README or Canva notes, here's the structure I recommend for **every program**, just like your previous notes.

---

# 🚗 Python OOP - Classes & Objects

# 🎯 Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **Classes** and **Objects**.

Instead of writing everything using functions, OOP groups **data (attributes)** and **behavior (methods)** together.

OOP makes programs:

* ✅ Reusable
* ✅ Organized
* ✅ Secure
* ✅ Easy to Maintain
* ✅ Easy to Scale

---

# 📖 What is a Class?

A **Class** is a blueprint (template) used to create objects.

A class contains:

* Attributes (Variables)
* Methods (Functions)

### Real World Example

Think of a **Car**.

A Car has:

**Attributes**

* Make
* Model
* Year

**Methods**

* Start()
* Stop()
* Display Info()

Car Blueprint

↓

Class

↓

Actual Car

↓

Object

---

# 📖 What is an Object?

An **Object** is an instance of a class.

Example

```python
car1 = Car("Toyota","Corolla",2020)
```

Here

Car

↓

Blueprint

car1

↓

Object

---

# 📖 What is a Constructor?

The constructor (`__init__()`) is a special method that is automatically called when an object is created.

Its purpose is to initialize object variables.

---

# 📖 What is self?

`self` refers to the current object.

It allows one object to access its own variables and methods.

---

# 🚗 Program 1 : Car Class

## 🎯 Problem Statement

Create a Car class that stores:

* Make
* Model
* Year

Display the car details.

---

## 📝 Code

```python
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
```

---

# 🧠 Logic Behind the Code

Step 1

Create a class called **Car**

↓

Step 2

Constructor receives

```
make
model
year
```

↓

Step 3

Store them inside object

```
self.make

self.model

self.year
```

↓

Step 4

display_info()

prints all details

---

# 🔍 Dry Run

### Object Creation

```python
car1 = Car("Toyota","Corolla",2020)
```

Constructor executes

```
self.make = Toyota

self.model = Corolla

self.year = 2020
```

Memory

```
car1

Make

Toyota

Model

Corolla

Year

2020
```

---

Calling

```python
car1.display_info()
```

prints

```
Make: Toyota

Model: Corolla

Year: 2020
```

---

# 📊 Flow Diagram

```text
Create Class
      │
      ▼
Create Object
      │
      ▼
Constructor Runs
      │
      ▼
Store Values
      │
      ▼
Call display_info()
      │
      ▼
Display Car Details
```

---

# 🌍 Real World Use Case

* Car Showroom Software
* Vehicle Registration
* Taxi Booking
* Car Rental System

---

# 🏦 Program 2 : Bank Account

## 🎯 Problem Statement

Create a Bank Account class that can

* Deposit money
* Withdraw money
* Check balance
* Display account details

---

## 🧠 Logic

When object is created

↓

Store

```
Account Number

Balance
```

↓

User Deposits

↓

Increase Balance

↓

User Withdraws

↓

Check

```
Balance >= Amount
```

If True

↓

Subtract

Else

↓

Show

```
Insufficient Balance
```

---

# 🔍 Dry Run

Initial Balance

```
5000
```

Deposit

```
3450
```

Balance

```
8450
```

Deposit

```
390
```

Balance

```
8840
```

Withdraw

```
4500
```

Balance

```
4340
```

---

# 📊 Flow Diagram

```text
Create Account
       │
       ▼
Store Account Number
       │
       ▼
Deposit Money
       │
       ▼
Increase Balance
       │
       ▼
Withdraw Money
       │
       ▼
Enough Balance?
    │          │
   Yes         No
    │          │
Subtract   Insufficient
    │
    ▼
Updated Balance
```

---

# 🌍 Real World Use Case

* ATM Machine
* Net Banking
* Mobile Banking
* UPI Applications

---

# 👨‍💼 Program 3 : Employee Class (Encapsulation)

## 🎯 Problem Statement

Store employee details securely.

Hide employee name using a private variable.

Access it only through Getter and Setter methods.

---

## 🧠 Logic

Employee Object

↓

Constructor

↓

Private Variable

```
__name
```

↓

Outside Class

Cannot Access Directly

↓

Getter

Returns Name

↓

Setter

Updates Name

---

# 🔍 Dry Run

Object Created

```python
emp1 = Employee("Yashwanth",902,60000)
```

Stores

```
__name = Yashwanth

emp_id = 902

salary = 60000
```

Calling

```python
emp1.get_name()
```

returns

```
Yashwanth
```

Calling

```python
emp1.set_name("Varun")
```

updates

```
Varun
```

Calling again

```python
emp1.get_name()
```

returns

```
Varun
```

---

# 📊 Encapsulation Diagram

```text
             Employee Object
          ┌────────────────────┐
          │ __name             │ 🔒 Private
          │ emp_id             │
          │ salary             │
          └────────────────────┘
                 ▲
                 │
        Getter / Setter
                 │
         Outside World
```

---

# 🌍 Real World Use Case

* Banking Passwords
* Employee Salary
* Login Credentials
* PIN Numbers

---

# 🔥 Public vs Private Variable

| Public Variable     | Private Variable             |
| ------------------- | ---------------------------- |
| Accessible anywhere | Accessible only inside class |
| `self.salary`       | `self.__name`                |
| Less secure         | More secure                  |

---

# 💡 Best Practices

✔ Use PascalCase for Class names

✔ Use meaningful variable names

✔ Keep sensitive data private

✔ One class should represent one object

✔ Use methods instead of writing everything in the constructor

✔ Keep business logic inside methods

---

# 🎤 Interview Questions

### 1. What is OOP?

OOP is a programming paradigm that organizes code using Classes and Objects.

---

### 2. What is a Class?

A class is a blueprint used to create objects.

---

### 3. What is an Object?

An object is an instance of a class.

---

### 4. What is a Constructor?

A constructor (`__init__`) initializes object variables automatically when an object is created.

---

### 5. What is self?

`self` refers to the current object of the class.

---

### 6. What is a Method?

A method is a function defined inside a class that operates on the object's data.

---

### 7. What is Encapsulation?

Encapsulation is the process of combining data and methods into one class while restricting direct access to sensitive data.

---

### 8. Why do we use Getter and Setter methods?

* To read private data safely (Getter)
* To modify private data safely (Setter)

---

### 9. Why is `__name` private?

Variables starting with `__` are intended to be private and cannot be accessed directly from outside the class.

---

### 10. Difference between Class and Object?

| Class             | Object            |
| ----------------- | ----------------- |
| Blueprint         | Instance          |
| Template          | Real object       |
| Defines structure | Holds actual data |

---

# 📌 Key Points to Remember

* ✅ OOP organizes code using **Classes** and **Objects**.
* ✅ A **Class** is a blueprint, while an **Object** is its instance.
* ✅ The **constructor (`__init__`)** initializes object attributes.
* ✅ `self` refers to the current object.
* ✅ A **method** is a function inside a class.
* ✅ **Encapsulation** protects data using private variables (`__variable`) and controlled access through getter/setter methods.
* ✅ OOP is widely used in real-world systems such as banking, e-commerce, healthcare, school management, and enterprise applications.

This format matches your previous README notes and is well suited for **GitHub**, **Canva**, and interview preparation.
