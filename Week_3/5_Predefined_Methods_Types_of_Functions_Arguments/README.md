This is a good summary. For interview preparation and Canva notes, I'd recommend a few corrections and additions to match current Python behavior.

---

# 📘 Python Dictionary Methods

## 📖 Definition

A **Dictionary** is a mutable collection that stores data as **key-value pairs**.

### 📝 Syntax

```python
student = {
    "id": 101,
    "name": "Ramesh",
    "course": "Python"
}
```

---

## 🔧 Dictionary Methods

| Method                      | Description                                                                                                                                        |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keys()`                    | Returns all dictionary keys.                                                                                                                       |
| `values()`                  | Returns all dictionary values.                                                                                                                     |
| `items()`                   | Returns all key-value pairs as tuples.                                                                                                             |
| `get(key, default)`         | Returns the value of a key. If the key doesn't exist, returns the default value (or `None`).                                                       |
| `update(other_dict)`        | Adds or updates key-value pairs from another dictionary.                                                                                           |
| `pop(key[, default])`       | Removes the specified key and returns its value. If a default is provided and the key is missing, returns the default instead of raising an error. |
| `popitem()`                 | Removes and returns the last inserted key-value pair (Python 3.7+).                                                                                |
| `clear()`                   | Removes all key-value pairs.                                                                                                                       |
| `copy()`                    | Creates a shallow copy of the dictionary.                                                                                                          |
| `setdefault(key, default)`  | Returns the value if the key exists; otherwise inserts the key with the default value.                                                             |
| `fromkeys(iterable, value)` | Creates a new dictionary with specified keys and a common value.                                                                                   |

---

# 🧩 Python Set

## 📖 Definition

A **Set** is an **unordered, mutable collection of unique elements**.

### 📝 Syntax

```python
numbers = {10, 20, 30, 40}
```

---

# 🔧 Set Methods

## ➕ Adding & Removing Elements

| Method             | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| `add(item)`        | Adds one element.                                          |
| `update(iterable)` | Adds multiple elements.                                    |
| `remove(item)`     | Removes an element. Raises `KeyError` if not found.        |
| `discard(item)`    | Removes an element. No error if not found.                 |
| `pop()`            | Removes and returns a random element (sets are unordered). |
| `clear()`          | Removes all elements.                                      |
| `copy()`           | Creates a shallow copy.                                    |

---

## 🔄 Set Operations

| Method                       | Description                                           |
| ---------------------------- | ----------------------------------------------------- |
| `union(set2)`                | Returns all unique elements from both sets.           |
| `intersection(set2)`         | Returns common elements.                              |
| `difference(set2)`           | Returns elements in the first set but not the second. |
| `symmetric_difference(set2)` | Returns elements present in either set, but not both. |
| `issubset(set2)`             | Checks if one set is a subset of another.             |
| `issuperset(set2)`           | Checks if one set is a superset of another.           |
| `isdisjoint(set2)`           | Returns `True` if two sets have no common elements.   |

---

# ❄️ Frozen Set

## 📖 Definition

A **Frozen Set** is an **immutable version of a Set**.

Once created, its elements cannot be added, removed, or modified.

### 📝 Syntax

```python
numbers = frozenset([10, 20, 30])
```

### ✅ Features

* Immutable
* Unique elements only
* Can be used as dictionary keys
* Supports set operations (`union()`, `intersection()`, etc.)

---

# ⚙️ Python Function

## 📖 Definition

A **Function** is a reusable block of code that performs a specific task and runs only when it is called.

### 📝 Syntax

```python
def function_name(parameters):
    # Function body
    return value

function_name(arguments)
```

---

# 🎯 Types of Function Arguments

## 1️⃣ Positional Arguments

### 📖 Definition

Arguments are passed in the same order as parameters.

### Example

```python
def greet(name, age):
    print(name, age)

greet("Ramesh", 25)
```

---

## 2️⃣ Default Arguments

### 📖 Definition

A parameter has a default value. If no argument is passed, the default value is used.

### Syntax

```python
def greet(name="Guest"):
    print(name)
```

### Example

```python
greet()
greet("Ramesh")
```

---

## 3️⃣ Keyword Arguments

### 📖 Definition

Arguments are passed using parameter names, so the order does not matter.

### Example

```python
def student(name, age):
    print(name, age)

student(age=25, name="Ramesh")
```

---

## 4️⃣ Variable Length Arguments (`*args`)

### 📖 Definition

Used when the number of positional arguments is unknown.

`*args` stores all extra arguments as a **tuple**.

### Syntax

```python
def function_name(*args):
    pass
```

### Example

```python
def add(*numbers):
    print(numbers)

add(10, 20, 30, 40)
```

**Output**

```python
(10, 20, 30, 40)
```

---

## 5️⃣ Keyword Variable Length Arguments (`**kwargs`)

### 📖 Definition

Used when the number of keyword arguments is unknown.

`**kwargs` stores all keyword arguments as a **dictionary**.

### Syntax

```python
def function_name(**kwargs):
    pass
```

### Example

```python
def student(**details):
    print(details)

student(name="Ramesh", age=25, city="Hyderabad")
```

**Output**

```python
{'name': 'Ramesh', 'age': 25, 'city': 'Hyderabad'}
```

---

# 📊 Summary Table

| Topic                | Purpose                               | Data Type  |
| -------------------- | ------------------------------------- | ---------- |
| `*args`              | Accept unlimited positional arguments | Tuple      |
| `**kwargs`           | Accept unlimited keyword arguments    | Dictionary |
| Default Arguments    | Optional parameter values             | Any        |
| Keyword Arguments    | Pass values by parameter name         | Any        |
| Positional Arguments | Pass values in order                  | Any        |

---

# 🎤 Frequently Asked Interview Questions

### 1. What is the difference between `remove()` and `discard()` in a Set?

| `remove()`                               | `discard()`             |
| ---------------------------------------- | ----------------------- |
| Raises `KeyError` if the item is missing | Does not raise an error |

---

### 2. What is the difference between `*args` and `**kwargs`?

| `*args`                     | `**kwargs`               |
| --------------------------- | ------------------------ |
| Stores positional arguments | Stores keyword arguments |
| Tuple                       | Dictionary               |

---

### 3. What is a Frozen Set?

An immutable version of a set that cannot be modified after creation.

---

### 4. What is the difference between `get()` and `[]` in a Dictionary?

| `get()`                                                 | `[]`                                    |
| ------------------------------------------------------- | --------------------------------------- |
| Returns `None` or a default value if the key is missing | Raises `KeyError` if the key is missing |

---

### 5. What is the difference between Positional and Keyword Arguments?

| Positional         | Keyword                  |
| ------------------ | ------------------------ |
| Order matters      | Order does not matter    |
| Passed by position | Passed by parameter name |

---

These notes are interview-ready, follow current Python standards, and fit well into a professional README or Canva study guide.
