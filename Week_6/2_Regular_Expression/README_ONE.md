This is an excellent RegEx practice file. I recommend organizing it in the same format as your OOP and Exception Handling notes.

Use this structure:

---

# 📘 Python Regular Expressions (RegEx)

## 📖 Definition

**Regular Expression (RegEx)** is a sequence of characters that defines a search pattern.

It is mainly used for:

* 🔍 Searching text
* ✅ Validating user input
* 🔄 Replacing text
* ✂️ Splitting strings
* 📄 Extracting data from text

Python provides the built-in **`re`** module to work with Regular Expressions.

---

# 🎯 Why Do We Use RegEx?

RegEx helps us perform pattern matching quickly.

### Real-Time Applications

* 📧 Email Validation
* 🔐 Password Validation
* 📱 Mobile Number Validation
* 🆔 Aadhaar Validation
* 💳 PAN Card Validation
* 👨‍💼 Employee ID Validation
* 🌐 Web Scraping
* 📝 Form Validation

---

# 📥 Import re Module

## 📌 Syntax

```python
import re
```

---

# 🔹 re.match()

## 📖 Definition

`re.match()` checks whether the **pattern matches from the beginning** of the string.

## ⚙️ Syntax

```python
re.match(pattern, string)
```

## 💻 Example

```python
import re

text = "Python Programming"

result = re.match("Python", text)

if result:
    print(result.group())
```

### 🖥️ Output

```
Python
```

---

# 🔹 re.search()

## 📖 Definition

`re.search()` searches the **entire string** and returns the first match.

## ⚙️ Syntax

```python
re.search(pattern, string)
```

## 💻 Example

```python
text = "Python is easy to learn"

result = re.search("easy", text)

if result:
    print(result.group())
```

### 🖥️ Output

```
easy
```

---

# 🔹 re.findall()

## 📖 Definition

Returns **all matches** as a list.

## ⚙️ Syntax

```python
re.findall(pattern, string)
```

## 💻 Example

```python
text = "Apple Mango Apple Orange Apple"

print(re.findall("Apple", text))
```

### 🖥️ Output

```
['Apple', 'Apple', 'Apple']
```

---

# 🔹 re.finditer()

## 📖 Definition

Returns an iterator containing all matches with their positions.

## ⚙️ Syntax

```python
re.finditer(pattern, string)
```

## 💻 Example

```python
text = "Apple Mango Apple Orange Apple"

for item in re.finditer("Apple", text):
    print(item.start(), item.end())
```

### 🖥️ Output

```
0 5
12 17
25 30
```

---

# 🔹 re.split()

## 📖 Definition

Splits a string wherever the pattern matches.

## ⚙️ Syntax

```python
re.split(pattern, string)
```

## 💻 Example

```python
text = "Python,Java,C++,JavaScript"

print(re.split(",", text))
```

### 🖥️ Output

```
['Python', 'Java', 'C++', 'JavaScript']
```

---

# 🔹 re.sub()

## 📖 Definition

Replaces matching text with another string.

## ⚙️ Syntax

```python
re.sub(pattern, replacement, string)
```

## 💻 Example

```python
text = "Python is awesome"

print(re.sub("awesome", "powerful", text))
```

### 🖥️ Output

```
Python is powerful
```

---

# 📧 Email Validation

## 📖 Definition

Checks whether an email follows the correct format.

## ⚙️ Pattern

```python
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

## 💻 Example

```python
hello@gmail.com
```

### 🖥️ Output

```
Valid
```

---

# 🔐 Password Validation

## 📖 Definition

Checks whether a password satisfies specific security rules.

### Rules

* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit

## ⚙️ Pattern

```python
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
```

---

# 📱 Mobile Number Validation

## 📖 Definition

Checks whether a mobile number starts with **6–9** and contains **10 digits**.

## ⚙️ Pattern

```python
mobile_pattern = r"^[6-9]\d{9}$"
```

---

# 🆔 Aadhaar Validation

## 📖 Definition

Checks whether an Aadhaar number contains exactly **12 digits**.

## ⚙️ Pattern

```python
aadhaar_pattern = r"^\d{12}$"
```

---

# 💳 PAN Card Validation

## 📖 Definition

Checks whether a PAN card follows the Indian PAN format.

## ⚙️ Pattern

```python
pan_pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
```

---

# 👨‍💼 Employee ID Validation

## 📖 Definition

Checks whether an employee ID starts with **EMP** followed by **4 digits**.

## ⚙️ Pattern

```python
emp_pattern = r"^EMP\d{4}$"
```

---

# 🔢 Digit Matching

## 📖 Definition

Extracts all digits from a string.

## 💻 Example

```python
text = "Employee Id : 12345"

print(re.findall(r"\d", text))
```

### 🖥️ Output

```
['1', '2', '3', '4', '5']
```

---

# 🔤 Alphabet Matching

## 📖 Definition

Extracts only alphabet characters.

## 💻 Example

```python
text = "Python123"

print(re.findall(r"[A-Za-z]", text))
```

### 🖥️ Output

```
['P', 'y', 't', 'h', 'o', 'n']
```

---

# 📚 Common RegEx Symbols

| Symbol | Meaning                  |
| ------ | ------------------------ |
| `^`    | Start of string          |
| `$`    | End of string            |
| `.`    | Any single character     |
| `*`    | Zero or more occurrences |
| `+`    | One or more occurrences  |
| `?`    | Zero or one occurrence   |
| `[]`   | Character set            |
| `{}`   | Number of repetitions    |
| `\d`   | Digit                    |
| `\D`   | Non-digit                |
| `\w`   | Word character           |
| `\W`   | Non-word character       |
| `\s`   | White space              |
| `\S`   | Non-white space          |

---

# 📝 Final Summary

✅ RegEx is used to search, validate, replace, and extract text.

✅ Python provides the **`re`** module.

### Important Functions

* `re.match()`
* `re.search()`
* `re.findall()`
* `re.finditer()`
* `re.split()`
* `re.sub()`

### Common Validations

* 📧 Email
* 🔐 Password
* 📱 Mobile Number
* 🆔 Aadhaar
* 💳 PAN Card
* 👨‍💼 Employee ID

---

# 🎤 Interview Questions

### 1. What is Regular Expression (RegEx)?

**Answer:** A Regular Expression is a sequence of characters that defines a search pattern. It is used for searching, validating, extracting, and replacing text.

---

### 2. Which module is used for Regular Expressions in Python?

**Answer:** The built-in `re` module.

---

### 3. What is the difference between `re.match()` and `re.search()`?

| `re.match()`                                          | `re.search()`                                       |
| ----------------------------------------------------- | --------------------------------------------------- |
| Checks only from the beginning of the string          | Searches the entire string                          |
| Returns a match only if the pattern starts at index 0 | Returns the first occurrence anywhere in the string |

---

### 4. What does `re.findall()` return?

**Answer:** It returns a list containing all matches of the pattern.

---

### 5. What is the purpose of `re.finditer()`?

**Answer:** It returns an iterator of match objects, allowing access to each match and its position.

---

### 6. What is `re.split()` used for?

**Answer:** It splits a string based on a specified pattern.

---

### 7. What is `re.sub()` used for?

**Answer:** It replaces matching text with another string.

---

### 8. Name some real-world applications of RegEx.

* Email validation
* Password validation
* Mobile number validation
* Aadhaar validation
* PAN card validation
* Employee ID validation
* Form validation
* Web scraping

---

## ⭐ Easy Memory Trick

Remember the six most important RegEx functions:

```text
📥 Import → import re
        │
        ▼
🔹 match()     → Beginning of string
🔹 search()    → Search anywhere
🔹 findall()   → Return all matches
🔹 finditer()  → Return matches with positions
🔹 split()     → Split the string
🔹 sub()       → Replace text
```

This structure matches the same style you've been using for OOP and Exception Handling, making your Python notes consistent and interview-ready.
