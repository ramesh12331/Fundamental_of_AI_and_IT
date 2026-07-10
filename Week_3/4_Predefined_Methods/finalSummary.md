## 📊 Difference Between Built-in Functions, List Comprehension, and Python Data Type Methods

| Feature                     | 🔧 Built-in Functions                   | ⚡ List Comprehension            | 📘 Dictionary Methods                 | 📋 List Methods                | 🧩 Set Methods                  | 🔤 String Methods                | 📦 Tuple Methods                |
| --------------------------- | --------------------------------------- | ------------------------------- | ------------------------------------- | ------------------------------ | ------------------------------- | -------------------------------- | ------------------------------- |
| **Definition**              | Predefined functions provided by Python | Short syntax for creating lists | Methods for working with dictionaries | Methods for working with lists | Methods for working with sets   | Methods for manipulating strings | Methods for working with tuples |
| **Works On**                | All supported data types                | Lists and iterables             | Dictionary (`dict`)                   | List (`list`)                  | Set (`set`)                     | String (`str`)                   | Tuple (`tuple`)                 |
| **Purpose**                 | Perform common operations               | Create/filter/transform lists   | Manage key-value pairs                | Add, remove, sort list items   | Perform unique value operations | Modify and validate text         | Access and analyze tuple data   |
| **Returns**                 | Depends on function                     | Always returns a new list       | Depends on method                     | Usually modifies list          | Depends on method               | Usually returns a new string     | Returns values or information   |
| **Modifies Original Data**  | Usually No                              | No                              | Some methods modify                   | Yes (most methods)             | Yes (most methods)              | No (strings are immutable)       | No (tuples are immutable)       |
| **Collection Type**         | Any                                     | List                            | Dictionary                            | List                           | Set                             | String                           | Tuple                           |
| **Supports Filtering**      | No                                      | Yes                             | No                                    | No                             | No                              | No                               | No                              |
| **Supports Transformation** | Limited                                 | Yes                             | Limited                               | Yes                            | Limited                         | Yes                              | No                              |
| **Common Interview Topic**  | ⭐⭐⭐⭐                                    | ⭐⭐⭐⭐⭐                           | ⭐⭐⭐⭐⭐                                 | ⭐⭐⭐⭐⭐                          | ⭐⭐⭐⭐                            | ⭐⭐⭐⭐⭐                            | ⭐⭐⭐⭐                            |

---

# 🔧 Built-in Functions

### 📖 Definition

Built-in functions are predefined functions provided by Python to perform common operations.

### ✅ Examples

```python
len()
sum()
max()
min()
list()
tuple()
type()
print()
input()
range()
```

### 💻 Example

```python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
```

---

# ⚡ List Comprehension

### 📖 Definition

List Comprehension is a short and efficient way to create a new list using a single line of code.

### 💻 Example

```python
numbers = [1,2,3,4,5]

squares = [num**2 for num in numbers]

print(squares)
```

**Output**

```text
[1,4,9,16,25]
```

---

# 📘 Dictionary Methods

### 📖 Definition

Dictionary methods are built-in methods used to create, access, update, and manage key-value pairs.

### ✅ Common Methods

```python
keys()
values()
items()
get()
update()
pop()
copy()
clear()
```

### 💻 Example

```python
student = {
    "name":"Ramesh"
}

print(student.get("name"))
```

---

# 📋 List Methods

### 📖 Definition

List methods are built-in methods used to add, remove, search, sort, and modify list elements.

### ✅ Common Methods

```python
append()
extend()
insert()
remove()
pop()
sort()
reverse()
copy()
```

### 💻 Example

```python
cities = ["Hyderabad"]

cities.append("Delhi")

print(cities)
```

---

# 🧩 Set Methods

### 📖 Definition

Set methods are used to perform operations on unique values stored in a set.

### ✅ Common Methods

```python
add()
update()
remove()
discard()
union()
intersection()
difference()
```

### 💻 Example

```python
numbers = {10,20}

numbers.add(30)

print(numbers)
```

---

# 🔤 String Methods

### 📖 Definition

String methods are built-in methods used to manipulate and validate text.

### ✅ Common Methods

```python
upper()
lower()
split()
join()
replace()
find()
count()
strip()
```

### 💻 Example

```python
name = "python"

print(name.upper())
```

---

# 📦 Tuple Methods

### 📖 Definition

Tuple methods are built-in methods used to access and analyze tuple elements.

Since tuples are immutable, they have very few methods.

### ✅ Common Methods

```python
count()
index()
len()
max()
min()
sum()
```

### 💻 Example

```python
numbers = (10,20,30)

print(numbers.count(20))
```

---

# 📊 Quick Comparison Table

| Feature        | Built-in Functions | List Comprehension    | Dictionary             | List         | Set                  | String          | Tuple           |
| -------------- | ------------------ | --------------------- | ---------------------- | ------------ | -------------------- | --------------- | --------------- |
| Purpose        | General operations | Create new lists      | Manage key-value pairs | Modify lists | Manage unique values | Manipulate text | Read tuple data |
| Mutable        | Depends            | No                    | ✅ Yes                  | ✅ Yes        | ✅ Yes                | ❌ No            | ❌ No            |
| Data Structure | Any                | List                  | Dictionary             | List         | Set                  | String          | Tuple           |
| Common Example | `len()`            | `[x*x for x in nums]` | `get()`                | `append()`   | `add()`              | `upper()`       | `count()`       |

---

# 🎤 Interview Questions

### 1. What is the difference between a Built-in Function and a Method?

| Built-in Function        | Method                          |
| ------------------------ | ------------------------------- |
| Called directly          | Called using an object          |
| Works on many data types | Belongs to a specific data type |
| Example: `len(list)`     | Example: `list.append(10)`      |

---

### 2. What is the difference between List Comprehension and a for loop?

| List Comprehension | for Loop                  |
| ------------------ | ------------------------- |
| Short and concise  | Longer code               |
| Creates a new list | Can perform any operation |
| Faster             | Slightly slower           |

---

### 3. Which data types are mutable?

* ✅ List
* ✅ Dictionary
* ✅ Set

---

### 4. Which data types are immutable?

* ✅ String
* ✅ Tuple

---

# 📌 Final Summary

| Topic                 | Main Purpose                               |
| --------------------- | ------------------------------------------ |
| 🔧 Built-in Functions | Perform common operations on data          |
| ⚡ List Comprehension  | Quickly create and filter lists            |
| 📘 Dictionary Methods | Manage key-value pairs                     |
| 📋 List Methods       | Add, remove, sort, and update list items   |
| 🧩 Set Methods        | Work with unique values and set operations |
| 🔤 String Methods     | Process and manipulate text                |
| 📦 Tuple Methods      | Access and analyze immutable collections   |

> 💡 **Easy Memory Trick**
>
> * 🔧 **Built-in Functions** → Work with **all data types**
> * ⚡ **List Comprehension** → **Create new lists**
> * 📋 **List Methods** → **Modify lists**
> * 📘 **Dictionary Methods** → **Manage key-value pairs**
> * 🧩 **Set Methods** → **Handle unique values**
> * 🔤 **String Methods** → **Manipulate text**
> * 📦 **Tuple Methods** → **Access immutable data**
