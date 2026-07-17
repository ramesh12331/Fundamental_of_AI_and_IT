This is the next important OOP topic after Classes and Encapsulation. Below is a **complete README/Canva-friendly explanation** matching the style of your previous Python notes.

---

# 📘 Python Inheritance

---

# 🎯 Introduction

**Inheritance** is one of the four main principles of Object-Oriented Programming (OOP).

It allows one class (**Child Class**) to inherit the properties and methods of another class (**Parent Class**).

Inheritance helps in:

* ✅ Code Reusability
* ✅ Reducing Duplicate Code
* ✅ Easier Maintenance
* ✅ Extending Existing Classes
* ✅ Building Hierarchical Relationships

---

# 📖 What is Inheritance?

### Definition

**Inheritance** is the process by which one class acquires the attributes and methods of another class.

The existing class is called the **Parent (Base) Class**, and the new class is called the **Child (Derived) Class**.

---

# 🌍 Real-World Example

Imagine a **Vehicle**.

All vehicles have common properties:

* Brand
* Wheels
* Start()

A **Bike** is also a vehicle, but it has an additional property:

* Color

Instead of rewriting the common code, the Bike class inherits from Vehicle.

```text
Vehicle
│
├── Brand
├── Wheels
└── Start()
        │
        ▼
Bike
│
├── Brand
├── Wheels
├── Start()
└── Color
```

---

# 📊 Parent vs Child Class

| Parent Class            | Child Class         |
| ----------------------- | ------------------- |
| Base Class              | Derived Class       |
| Existing Class          | New Class           |
| Common Features         | Additional Features |
| Can exist independently | Depends on Parent   |

---

# ⭐ Advantages of Inheritance

* Code Reusability
* Easy Code Maintenance
* Reduces Duplicate Code
* Supports Code Extension
* Improves Readability

---

# 📝 Basic Syntax

```python
class Parent:

    def __init__(self):
        pass


class Child(Parent):

    def __init__(self):
        super().__init__()
```

---

# 🚗 Example 1: Basic Inheritance

```python
class A:

    def __init__(self):
        self.x = 10


class B(A):

    def __init__(self):
        super().__init__()
        self.y = 20


b = B()

print(b.x)
print(b.y)
```

---

# 🧠 Logic Behind the Code

### Step 1

Create Parent Class

```text
Class A

↓

x = 10
```

---

### Step 2

Create Child Class

```text
Class B

↓

inherits A
```

---

### Step 3

`super().__init__()` executes Parent Constructor.

```text
Parent Constructor

↓

self.x = 10
```

---

### Step 4

Child Constructor executes.

```text
self.y = 20
```

---

### Step 5

Object Created

Memory

```text
Object b

x = 10

y = 20
```

---

# 🔍 Dry Run

Object Creation

```python
b = B()
```

Python executes

```text
B Constructor

↓

super()

↓

A Constructor

↓

x = 10

↓

Back to B

↓

y = 20
```

Output

```text
10

20
```

---

# 📊 Flow Diagram

```text
Create Object

↓

Child Constructor

↓

super()

↓

Parent Constructor

↓

Initialize Parent Variables

↓

Back to Child

↓

Initialize Child Variables

↓

Object Ready
```

---

# 🚲 Example 2: Vehicle and Bike

```python
class Vehicle:

    def __init__(self, brand, wheels):

        self.brand = brand
        self.wheels = wheels

    def show_info(self):

        print(self.brand)
```

---

Child Class

```python
class Bike(Vehicle):

    def __init__(self, brand, wheels, color):

        super().__init__(brand, wheels)

        self.color = color
```

---

Object

```python
bike = Bike("Yamaha",2,"Red")
```

---

Memory

```text
Bike Object

Brand

Yamaha

Wheels

2

Color

Red
```

---

Output

```text
Brand: Yamaha

Wheels: 2

Color: Red
```

---

# 🧠 Why Use `super()`?

### Definition

`super()` is a built-in function that calls the **immediate parent class** constructor or methods.

### Syntax

```python
super().__init__()
```

### Why?

Without `super()`, the parent class constructor is **not executed automatically**.

Using `super()` avoids rewriting parent initialization code.

---

# 🔍 Dry Run for `super()`

```text
Bike Object Created

↓

Bike Constructor

↓

super()

↓

Vehicle Constructor

↓

brand = Yamaha

wheels = 2

↓

Back to Bike

↓

color = Red
```

---

# 🚗 Example 3: Multi-Level Inheritance

```python
VehicleBase

↓

Car

↓

ElectricCar
```

Code

```python
tesla = ElectricCar()
```

Methods Available

```text
start()

drive()

charge()
```

---

# Dry Run

```text
ElectricCar Object

↓

VehicleBase.start()

↓

Car.drive()

↓

ElectricCar.charge()
```

Output

```text
Vehicle started

Car is driving

Battery charging
```

---

# 📊 Types of Inheritance

## 1. Single Inheritance

```text
A

↓

B
```

---

## 2. Multi-Level Inheritance

```text
A

↓

B

↓

C
```

Example

Vehicle

↓

Car

↓

ElectricCar

---

## 3. Hierarchical Inheritance

```text
        A

   ┌────┼────┐

   B    C    D
```

One parent has multiple child classes.

---

## 4. Multiple Inheritance *(Python Supports It)*

```text
A      B

 \    /

   C
```

A child class inherits from more than one parent class.

---

## 5. Hybrid Inheritance

A combination of two or more inheritance types.

---

# 🌍 Real-World Applications

* Vehicle Management Systems
* Banking Applications
* School Management Systems
* Hospital Management Systems
* E-commerce Platforms
* Game Development

---

# 💡 Best Practices

* Use inheritance only when there is an **"is-a" relationship**.
* Call `super().__init__()` to initialize parent attributes.
* Keep parent classes generic and reusable.
* Avoid deep inheritance chains unless necessary.
* Use meaningful class names.

---

# 🎤 Interview Questions & Answers

### 1. What is Inheritance?

Inheritance is the process where one class acquires the properties and methods of another class.

---

### 2. What is a Parent Class?

A Parent (Base) Class is the class whose attributes and methods are inherited by another class.

---

### 3. What is a Child Class?

A Child (Derived) Class inherits the attributes and methods of a Parent Class and can also have its own features.

---

### 4. What is `super()`?

`super()` is used to call the immediate parent class constructor or methods.

---

### 5. Why do we use `super().__init__()`?

To initialize the parent class attributes without rewriting the parent constructor.

---

### 6. What are the advantages of inheritance?

* Code Reusability
* Easy Maintenance
* Reduced Code Duplication
* Better Organization
* Extensibility

---

### 7. How many types of inheritance are there in Python?

1. Single Inheritance
2. Multi-Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance

---

### 8. Difference between Single and Multi-Level Inheritance?

| Single Inheritance       | Multi-Level Inheritance                       |
| ------------------------ | --------------------------------------------- |
| One parent and one child | A chain of inheritance across multiple levels |
| `A → B`                  | `A → B → C`                                   |

---

### 9. What is the difference between a Parent Class and a Child Class?

| Parent Class                  | Child Class                             |
| ----------------------------- | --------------------------------------- |
| Provides common functionality | Reuses and extends parent functionality |
| Also called Base Class        | Also called Derived Class               |

---

# 📋 Final Summary

```text
Python Inheritance
│
├── Parent Class (Base)
│
├── Child Class (Derived)
│
├── super()
│
├── Code Reusability
│
├── Single Inheritance
│
├── Multi-Level Inheritance
│
├── Hierarchical Inheritance
│
├── Multiple Inheritance
│
└── Hybrid Inheritance
```

## Key Takeaways

* ✅ **Inheritance** allows a child class to reuse the attributes and methods of a parent class.
* ✅ **`super()`** calls the immediate parent class constructor or methods, ensuring parent attributes are initialized correctly.
* ✅ It reduces duplicate code and improves maintainability.
* ✅ Python supports **five types of inheritance**: Single, Multi-Level, Hierarchical, Multiple, and Hybrid.
* ✅ Inheritance is ideal for modeling **"is-a" relationships**, such as `Bike is a Vehicle` or `ElectricCar is a Car`.
