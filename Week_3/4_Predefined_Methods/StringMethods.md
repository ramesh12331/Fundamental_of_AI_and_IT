This chapter should follow the same **Canva README.md** style as your previous notes.

---

# 🔤 Python String Methods

> 🚀 **Complete Beginner to Interview Guide** with **Definition, Features, Syntax, Example, Output, Logic Behind the Code, Dry Run, Flow Diagram, Real-World Examples, Best Practices, Interview Questions, and Final Summary.**

---

# 📚 Table of Contents

* 🎯 Introduction
* 📖 What is a String?
* ⭐ Features
* 📝 Syntax
* 🔤 String Methods
* 🌍 Real-World Applications
* 💡 Best Practices
* 🎤 Interview Questions
* 📌 Key Points
* 📋 Final Summary

---

# 🎯 Introduction

A **String** is one of the most commonly used data types in Python. It stores text data and provides many built-in methods to format, search, validate, split, join, and manipulate text.

---

# 📖 What is a String?

A **String (`str`)** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` / `""" """`).

### 💻 Example

```python
name = "Python"
```

---

# ⭐ Features

* ✅ Immutable (cannot be modified directly)
* ✅ Ordered sequence
* ✅ Supports indexing and slicing
* ✅ Rich collection of built-in methods
* ✅ Supports Unicode characters

---

# 📝 Syntax

```python
string_name = "Hello World"
```

---

# 🔤 A. Case Conversion Methods

## 📘 1. upper()

### 🎯 Definition

Converts all lowercase letters to uppercase.

### ⭐ Syntax

```python
string.upper()
```

### 💻 Example

```python
announcement = "The office will remain closed."

print(announcement.upper())
```

### 🖥 Output

```text
THE OFFICE WILL REMAIN CLOSED.
```

### 🧠 Logic Behind the Code

```text
Original String
      │
      ▼
upper()
      │
      ▼
All Letters → UPPERCASE
```

### 🌍 Real-World Use Case

* Certificates
* Usernames
* Reports

---

## 📘 2. lower()

### 🎯 Definition

Converts all uppercase letters to lowercase.

### ⭐ Syntax

```python
string.lower()
```

### 💻 Example

```python
print(announcement.lower())
```

### 🖥 Output

```text
the office will remain closed.
```

---

## 📘 3. capitalize()

### 🎯 Definition

Capitalizes only the first character of the string.

### ⭐ Syntax

```python
string.capitalize()
```

### 💻 Example

```python
name = "hari krishna"

print(name.capitalize())
```

### 🖥 Output

```text
Hari krishna
```

---

## 📘 4. title()

### 🎯 Definition

Capitalizes the first letter of every word.

### ⭐ Syntax

```python
string.title()
```

### 💻 Example

```python
print(name.title())
```

### 🖥 Output

```text
Hari Krishna
```

---

## 📘 5. swapcase()

### 🎯 Definition

Converts uppercase letters to lowercase and lowercase letters to uppercase.

### ⭐ Syntax

```python
string.swapcase()
```

### 💻 Example

```python
announcement = "The Office Will Remain Closed"

print(announcement.swapcase())
```

### 🖥 Output

```text
tHE oFFICE wILL rEMAIN cLOSED
```

---

# 🔍 B. String Checking Methods

## 📘 6. isalpha()

### 🎯 Definition

Returns **True** if all characters are alphabets.

### ⭐ Syntax

```python
string.isalpha()
```

### 💻 Example

```python
name = "AmitabhBachan"

print(name.isalpha())
```

### 🖥 Output

```text
True
```

---

## 📘 7. isdigit()

### 🎯 Definition

Returns **True** if all characters are digits.

### ⭐ Syntax

```python
string.isdigit()
```

### 💻 Example

```python
aadhar = "985689002345A"

print(aadhar.isdigit())
```

### 🖥 Output

```text
False
```

---

## 📘 8. isalnum()

### 🎯 Definition

Returns **True** if all characters are letters or digits.

### ⭐ Syntax

```python
string.isalnum()
```

### 💻 Example

```python
pan = "ABCDE1234F"

print(pan.isalnum())
```

### 🖥 Output

```text
True
```

---

## 📘 9. isspace()

### 🎯 Definition

Returns **True** if the string contains only whitespace.

### ⭐ Syntax

```python
string.isspace()
```

### 💻 Example

```python
address = "  Hyderabad"

print(address.isspace())
```

### 🖥 Output

```text
False
```

---

## 📘 10. startswith()

### 🎯 Definition

Checks whether the string starts with a given prefix.

### ⭐ Syntax

```python
string.startswith(prefix)
```

### 💻 Example

```python
url = "https://datavalley.ai"

print(url.startswith("https://"))
```

### 🖥 Output

```text
True
```

---

## 📘 11. endswith()

### 🎯 Definition

Checks whether the string ends with a given suffix.

### ⭐ Syntax

```python
string.endswith(suffix)
```

### 💻 Example

```python
print(url.endswith(".ai"))
```

### 🖥 Output

```text
True
```

---

# 🔍 C. Searching & Replacing

## 📘 12. find()

### 🎯 Definition

Returns the index of a substring.

Returns **-1** if not found.

### ⭐ Syntax

```python
string.find(substring)
```

### 💻 Example

```python
address = "123 MG Road, Hyderabad"

print(address.find("Hyderabad"))
```

### 🖥 Output

```text
13
```

---

## 📘 13. index()

### 🎯 Definition

Returns the index of a substring.

Raises **ValueError** if not found.

### ⭐ Syntax

```python
string.index(substring)
```

### 💻 Example

```python
address.index("Hyderabad")
```

---

## 📘 14. count()

### 🎯 Definition

Counts how many times a substring appears.

### ⭐ Syntax

```python
string.count(substring)
```

### 💻 Example

```python
article = "India is in South Asia. India is a democratic country."

print(article.count("India"))
```

### 🖥 Output

```text
2
```

---

## 📘 15. replace()

### 🎯 Definition

Replaces occurrences of one substring with another.

### ⭐ Syntax

```python
string.replace(old,new)
```

### 💻 Example

```python
article = "India is beautiful"

print(article.replace("India","Bharat"))
```

### 🖥 Output

```text
Bharat is beautiful
```

---

# ✂️ D. Splitting & Joining

## 📘 16. split()

### 🎯 Definition

Splits a string into a list.

### ⭐ Syntax

```python
string.split(separator)
```

### 💻 Example

```python
student = "Keerthi Palagala"

print(student.split())
```

### 🖥 Output

```text
['Keerthi', 'Palagala']
```

---

## 📘 17. join()

### 🎯 Definition

Joins list elements into a single string.

### ⭐ Syntax

```python
separator.join(list)
```

### 💻 Example

```python
names = ["Keerthi","Palagala"]

print(" ".join(names))
```

### 🖥 Output

```text
Keerthi Palagala
```

---

# 📘 18. list()

### 🎯 Definition

Converts an iterable into a list.

### ⭐ Syntax

```python
list(iterable)
```

### 💻 Example

```python
mobile = "9032345245"

print(list(mobile))
```

### 🖥 Output

```text
['9','0','3','2','3','4','5','2','4','5']
```

---

# 📊 Flow Diagram

```text
            String
               │
   ┌───────────┼────────────┐
   ▼           ▼            ▼
Format      Validate      Search
 │            │            │
upper()    isalpha()     find()
lower()    isdigit()     index()
title()    isalnum()     count()
swapcase() startswith()  replace()
 │
 ▼
Split & Join
 │
split()
join()
 │
 ▼
Output
```

---

# 🌍 Real-World Applications

* 👤 Username formatting
* 📧 Email validation
* 🌐 URL checking
* 📄 Text processing
* 🔍 Search functionality
* 🤖 NLP (Natural Language Processing)
* 📊 Data cleaning
* 📱 Form validation

---

# 💡 Best Practices

* ✅ Use `upper()` and `lower()` for case-insensitive comparisons.
* ✅ Use `strip()` before processing user input.
* ✅ Use `find()` when a missing substring is acceptable.
* ✅ Use `index()` only when you're sure the substring exists.
* ✅ Use `join()` instead of repeated string concatenation.

---

# 🎤 Interview Questions

### 1. What is a String?

A sequence of characters enclosed in quotes.

---

### 2. Are Strings mutable?

No. Strings are immutable.

---

### 3. Difference between `find()` and `index()`?

| `find()`                  | `index()`                        |
| ------------------------- | -------------------------------- |
| Returns `-1` if not found | Raises `ValueError` if not found |

---

### 4. Difference between `split()` and `join()`?

| `split()`     | `join()`      |
| ------------- | ------------- |
| String → List | List → String |

---

### 5. Difference between `upper()` and `title()`?

| `upper()`     | `title()`                           |
| ------------- | ----------------------------------- |
| All uppercase | First letter of each word uppercase |

---

### 6. What does `isalnum()` check?

It returns `True` if the string contains only letters and digits.

---

# 📌 Key Points to Remember

* 📝 Strings are immutable.
* 🔠 `upper()`, `lower()`, `title()` change letter case.
* ✅ `isalpha()`, `isdigit()`, `isalnum()` validate text.
* 🔍 `find()` and `index()` search substrings.
* 🔄 `replace()` substitutes text.
* ✂️ `split()` converts a string to a list.
* 🔗 `join()` combines list elements into a string.
* 📋 `list()` converts an iterable into a list.

---

# 📋 Final Summary

| 🔧 Method      | 🎯 Purpose                               |
| -------------- | ---------------------------------------- |
| `upper()`      | Convert to uppercase                     |
| `lower()`      | Convert to lowercase                     |
| `capitalize()` | Capitalize first letter                  |
| `title()`      | Capitalize every word                    |
| `swapcase()`   | Reverse letter case                      |
| `isalpha()`    | Check letters only                       |
| `isdigit()`    | Check digits only                        |
| `isalnum()`    | Check letters and digits                 |
| `isspace()`    | Check whitespace only                    |
| `startswith()` | Check prefix                             |
| `endswith()`   | Check suffix                             |
| `find()`       | Find substring                           |
| `index()`      | Find substring (raises error if missing) |
| `count()`      | Count substring occurrences              |
| `replace()`    | Replace text                             |
| `split()`      | Convert string to list                   |
| `join()`       | Convert list to string                   |
| `list()`       | Convert iterable to list                 |

# 🎯 Key Takeaways

* 🚀 String methods simplify text processing and validation.
* 🔍 Use checking methods to validate user input.
* 🔄 Use searching and replacing methods for text manipulation.
* ✂️ `split()` and `join()` are essential for handling structured text.
* 🎯 String methods are widely used in **Python development, Data Science, Automation, AI, NLP, and technical interviews**.
