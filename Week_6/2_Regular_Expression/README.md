# 📘 README.md

# 🚀 Python Regular Expressions (RegEx) in Python

### Complete Beginner Guide with Examples, Syntax, Interview Questions & Cheat Sheet

---

# 📑 Table of Contents

1. Introduction
2. What is RegEx?
3. Why Use RegEx?
4. Importing re Module
5. Basic Syntax
6. Common RegEx Functions
7. Regular Expression Symbols
8. Character Classes
9. Quantifiers
10. Anchors
11. Email Validation
12. Password Validation
13. Mobile Number Validation
14. Aadhaar Validation
15. PAN Card Validation
16. Employee ID Validation
17. Search vs Match
18. Findall vs Finditer
19. Split()
20. Sub()
21. Practical Examples
22. Best Practices
23. Common Mistakes
24. Interview Questions & Answers
25. RegEx Cheat Sheet
26. Final Summary

---

# 📖 1. Introduction

Regular Expressions (RegEx) are special patterns used to search, match, validate, split, or replace text.

Python provides a built-in module named:

```python
import re
```

using this module, we can easily work with text.

---

# 🎯 2. What is RegEx?

Regular Expression is a sequence of characters that defines a search pattern.

It is mainly used for:

✅ Searching Text

✅ Validating Input

✅ Replacing Text

✅ Extracting Data

✅ Splitting Strings

---

## Example

```python
import re

text = "Python is easy"

result = re.search("easy", text)

print(result.group())
```

Output

```
easy
```

---

# ❓ Why Use Regular Expressions?

Instead of checking text manually,

```python
if "@" in email:
```

we can validate properly

```python
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

This checks the complete email format.

---

# 📦 3. Importing re Module

```python
import re
```

The re module contains all Regular Expression functions.

---

# ⚙️ 4. Basic Syntax

```python
re.function(pattern, string)
```

Example

```python
import re

text = "Python"

print(re.search("Python", text))
```

---

# 🛠️ 5. Common Functions

| Function       | Purpose                     |
| -------------- | --------------------------- |
| re.search()    | Finds first occurrence      |
| re.match()     | Checks beginning of string  |
| re.findall()   | Returns all matches         |
| re.finditer()  | Returns iterator of matches |
| re.split()     | Splits string               |
| re.sub()       | Replaces text               |
| re.compile()   | Compiles regex pattern      |
| re.fullmatch() | Matches entire string       |

---

# 🔎 6. re.search()

Searches anywhere in the string.

Syntax

```python
re.search(pattern, string)
```

Example

```python
import re

text="Python is easy"

result=re.search("easy",text)

print(result.group())
```

Output

```
easy
```

---

# 🎯 7. re.match()

Checks only beginning.

Example

```python
text="Python Programming"

print(re.match("Python",text))
```

Output

```
Matched
```

---

# 📋 8. re.findall()

Returns all matches.

Example

```python
text="Apple Mango Apple"

print(re.findall("Apple",text))
```

Output

```
['Apple', 'Apple']
```

---

# 🔄 9. re.finditer()

Returns iterator.

Example

```python
text="Apple Apple"

for item in re.finditer("Apple",text):
    print(item.start(), item.end())
```

Output

```
0 5
6 11
```

---

# ✂️ 10. re.split()

Splits string.

Example

```python
text="Python,Java,C++"

print(re.split(",",text))
```

Output

```
['Python', 'Java', 'C++']
```

---

# 🔁 11. re.sub()

Replace text.

Example

```python
text="Python is awesome"

print(re.sub("awesome","powerful",text))
```

Output

```
Python is powerful
```

---

# 📚 12. Character Classes

| Pattern | Meaning         |
| ------- | --------------- |
| \d      | Digit           |
| \D      | Non-digit       |
| \w      | Word character  |
| \W      | Non-word        |
| \s      | White space     |
| \S      | Non-white space |
| [abc]   | a,b,c           |
| [A-Z]   | Uppercase       |
| [a-z]   | Lowercase       |
| [0-9]   | Digits          |

Example

```python
re.findall(r"\d","abc123")
```

Output

```
['1','2','3']
```

---

# 🔢 13. Quantifiers

| Symbol | Meaning         |
| ------ | --------------- |
| *      | 0 or more       |
| +      | 1 or more       |
| ?      | 0 or 1          |
| {3}    | Exactly 3       |
| {2,5}  | Between 2 and 5 |
| {2,}   | 2 or more       |

Example

```python
re.findall(r"\d{3}","123456")
```

Output

```
123
456
```

---

# 📍 14. Anchors

| Symbol | Meaning |
| ------ | ------- |
| ^      | Start   |
| $      | End     |

Example

```python
re.match("^Python","Python Programming")
```

---

# 📧 15. Email Validation

Pattern

```python
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

Example

```python
email="hello@gmail.com"

if re.match(pattern,email):
    print("Valid")
```

---

# 🔒 16. Password Validation

Rules

✔ Minimum 8 characters

✔ Uppercase

✔ Lowercase

✔ Number

Pattern

```python
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$
```

---

# 📱 17. Mobile Number Validation

```python
^[6-9]\d{9}$
```

Valid

```
9876543210
```

Invalid

```
1234567890
```

---

# 🆔 18. Aadhaar Validation

Pattern

```python
^\d{12}$
```

---

# 💳 19. PAN Card Validation

Pattern

```python
^[A-Z]{5}[0-9]{4}[A-Z]$
```

Example

```
ABCDE1234F
```

---

# 👨‍💼 20. Employee ID Validation

Pattern

```python
^EMP\d{4}$
```

Example

```
EMP1001
```

---

# 💡 21. Practical Examples

## Extract Digits

```python
text="Employee123"

print(re.findall(r"\d",text))
```

---

## Extract Letters

```python
text="Python123"

print(re.findall(r"[A-Za-z]",text))
```

---

## Replace Word

```python
text="Python is awesome"

print(re.sub("awesome","powerful",text))
```

---

## Split CSV

```python
text="A,B,C,D"

print(re.split(",",text))
```

---

# ⭐ 22. Best Practices

✅ Always use raw strings

```python
r"\d+"
```

instead of

```python
"\\d+"
```

---

✅ Compile regex if reused many times.

```python
pattern=re.compile(r"\d+")
```

---

✅ Keep patterns simple.

---

# ❌ 23. Common Mistakes

Wrong

```python
"\d"
```

Correct

```python
r"\d"
```

---

Wrong

```python
re.match("abc","xyzabc")
```

Correct

```python
re.search("abc","xyzabc")
```

---

# 🎤 24. Interview Questions & Answers

---

## Q1. What is Regular Expression?

Answer:

Regular Expression is a search pattern used for searching, matching, replacing, and validating text.

---

## Q2. Which module is used?

Answer

```python
re
```

---

## Q3. Difference between search() and match()?

search()

Searches entire string.

match()

Checks only beginning.

---

## Q4. Difference between findall() and finditer()?

findall()

Returns list.

finditer()

Returns iterator.

---

## Q5. What does \d mean?

Answer

Digit

---

## Q6. Difference between * and + ?

*

Zero or More

*

One or More

---

## Q7. What is ^ ?

Beginning of string.

---

## Q8. What is $ ?

End of string.

---

## Q9. What is re.sub()?

Used for replacing text.

---

## Q10. What is re.split()?

Splits a string using a pattern.

---

## Q11. Why use raw strings (`r""`)?

Raw strings prevent Python from interpreting backslashes as escape characters, making regex patterns easier to read and write.

---

## Q12. What is `re.fullmatch()`?

It checks whether the **entire string** matches the pattern.

Example:

```python
import re

print(re.fullmatch(r"\d{4}", "1234"))
```

Output:

```
<re.Match object>
```

---

# 📚 25. Regular Expression Cheat Sheet

| Symbol | Meaning            |
| ------ | ------------------ |
| ^      | Start              |
| $      | End                |
| .      | Any character      |
| *      | 0 or More          |
| +      | 1 or More          |
| ?      | Optional           |
| \d     | Digit              |
| \D     | Non Digit          |
| \w     | Word Character     |
| \W     | Non Word Character |
| \s     | White Space        |
| \S     | Non White Space    |
| [abc]  | Character Set      |
| [A-Z]  | Uppercase          |
| [a-z]  | Lowercase          |
| [0-9]  | Digits             |
| {n}    | Exactly n          |
| {m,n}  | Range              |
| |      | OR                 |
| ()     | Grouping           |

---

# 📝 26. Final Summary

🎉 Congratulations! You have learned the fundamentals of Python Regular Expressions.

### ✅ Key Takeaways

* 📦 Import the `re` module to work with regular expressions.
* 🔍 Use `re.search()` to find the first occurrence anywhere in a string.
* 🎯 Use `re.match()` to check the beginning of a string.
* 📋 Use `re.findall()` to retrieve all matching patterns as a list.
* 🔄 Use `re.finditer()` to iterate through matches with position details.
* ✂️ Use `re.split()` to split text based on a pattern.
* 🔁 Use `re.sub()` to replace matching text with new text.
* 📧 Validate formats like Email, Password, Mobile Number, Aadhaar, PAN Card, and Employee IDs using regex.
* 🧩 Learn and apply special symbols (`^`, `$`, `.`, `*`, `+`, `?`, `\d`, `\w`, etc.) effectively.
* 💡 Prefer raw strings (`r"pattern"`) for writing regex patterns.
* ⚡ Compile frequently used patterns with `re.compile()` for better performance.

---

# 🏆 Learning Outcome

After completing this project, you can confidently:

* ✔ Search text using regular expressions
* ✔ Validate user inputs (Email, Password, Phone, PAN, Aadhaar, etc.)
* ✔ Extract information from strings
* ✔ Replace and split text efficiently
* ✔ Write clean and reusable regex patterns
* ✔ Answer common Python RegEx interview questions

---

# 📌 Author

**Mamidi Ramesh**

**Python | Full Stack Developer | Learning GCP + Python + AI**

⭐ *If you found this project useful, consider giving it a star on GitHub!*
