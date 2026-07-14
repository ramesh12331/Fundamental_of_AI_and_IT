This is enough content for a complete **Python File Handling, Date & Time, and CSV Module** chapter. Like your previous notes, I recommend organizing it as a Canva-ready README.

---

# 📘 Python Date & Time, File Handling & CSV Module

# 🎯 Introduction

Python provides powerful built-in modules to work with:

* 📅 Date & Time
* 📂 Files
* 📊 CSV Files

These are widely used in real-world applications such as attendance systems, banking software, payroll systems, data analysis, and report generation.

---

# 📚 Topics Covered

## 📖 Chapter 1: Python datetime Module

### Topics

* What is datetime?
* Why use datetime?
* Import datetime
* Current Date & Time
* Formatting Date & Time
* UTC Time
* strftime()

---

## 📖 Definition

The **datetime** module provides classes and methods to work with dates, times, timestamps, and time zones.

---

## ⭐ Features

* Get current date
* Get current time
* Format date & time
* Work with UTC time
* Calculate date differences
* Time zone support

---

## 📝 Syntax

```python
import datetime

current_time = datetime.datetime.now()
```

---

# 💻 Example 1 : Current Date & Time

```python
import datetime

current_time = datetime.datetime.now()

print(current_time)
```

---

## 🧠 Line-by-Line Explanation

```python
import datetime
```

Imports the built-in datetime module.

↓

```python
current_time = datetime.datetime.now()
```

Gets the current system date and time.

↓

```python
print(current_time)
```

Displays current date and time.

---

## 📊 Flow Diagram

```text
Import datetime

        │

        ▼

datetime.now()

        │

        ▼

Current Date & Time

        │

        ▼

Print
```

---

## 🖥 Output

```text
2026-07-14 15:32:48
```

---

# Example 2 : strftime()

## 📖 Definition

`strftime()` formats a date and time into a readable string.

---

## 📝 Syntax

```python
datetime.strftime(format)
```

---

## 💻 Program

```python
import datetime

current_time = datetime.datetime.now()

print(current_time.strftime("%H:%M:%S"))
```

---

## Output

```text
15:32:48
```

---

## Common Format Codes

| Format | Meaning        | Example |
| ------ | -------------- | ------- |
| `%H`   | Hour (24-hour) | 15      |
| `%I`   | Hour (12-hour) | 03      |
| `%M`   | Minutes        | 32      |
| `%S`   | Seconds        | 48      |
| `%d`   | Day            | 14      |
| `%m`   | Month          | 07      |
| `%Y`   | Year           | 2026    |
| `%A`   | Weekday        | Tuesday |
| `%B`   | Month Name     | July    |
| `%p`   | AM/PM          | PM      |
| `%Z`   | Time Zone      | UTC     |
| `%z`   | UTC Offset     | +0000   |

---

# Example 3 : Date Formatting

```python
print(current_time.strftime("%d-%m-%Y"))
```

Output

```text
14-07-2026
```

---

# Example 4 : Full Date

```python
print(current_time.strftime("%A, %B %d, %Y"))
```

Output

```text
Tuesday, July 14, 2026
```

---

# Example 5 : UTC Time

```python
from datetime import datetime, timezone

current_time_utc = datetime.now(timezone.utc)

print(current_time_utc.strftime("%I:%M:%S %p %Z %z"))
```

Output

```text
03:32:48 PM UTC +0000
```

---

# 🌍 Real World Example

Attendance System

```text
Employee Login

↓

Current Time

↓

Store Login Time

↓

Attendance Report
```

---

# 📘 Chapter 2 : File Handling

---

## 📖 Definition

File Handling allows Python programs to create, read, write, and append data to files.

---

## ⭐ Features

* Read files
* Write files
* Append data
* Binary file support
* Automatic resource management

---

## 📊 Flow Diagram

```text
Open File

↓

Read / Write

↓

Save

↓

Close File
```

---

## open()

### Syntax

```python
file = open(filename, mode)
```

---

## File Modes

| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| rb   | Read Binary  |
| wb   | Write Binary |

---

# Example : Read File

```python
india_file = open("india.txt","r")

content = india_file.readlines()

print(content)

india_file.close()
```

---

## Logic

```text
Open File

↓

Read All Lines

↓

Store in List

↓

Print

↓

Close File
```

---

# Example : Write File

```python
india_file = open("india.txt","w")

india_file.write("Hello Python")

india_file.close()
```

---

# Example : Append File

```python
india_file = open("india.txt","a")

india_file.write("\nIndia is a great country.")

india_file.close()
```

---

# writelines()

```python
india_file.writelines([
"\nIndia",
"\nPython"
])
```

Adds multiple lines at once.

---

# Why close()?

Always close the file because it

* Saves data
* Releases memory
* Prevents corruption

---

# with open()

## Recommended Method

```python
with open("india.txt","r") as india_file:

    content = india_file.readlines()

    print(content)
```

Python automatically closes the file.

---

## Why use with?

* No need to call `close()`
* Safer
* Cleaner code
* Recommended by Python

---

# Binary Files

```python
with open("Flag_of_India.webp","rb") as flag_file:

    content = flag_file.read()

    print(content)
```

Used for

* Images
* Videos
* PDFs
* Audio

---

# 📘 Chapter 3 : CSV Module

---

## 📖 Definition

CSV stands for **Comma-Separated Values**.

CSV files store tabular data like Excel spreadsheets.

---

## Import

```python
import csv
```

---

# Read CSV

```python
with open("students.csv","r") as students_file:

    csv_reader = csv.reader(students_file)

    for row in csv_reader:

        print(row)
```

---

# DictReader

```python
csv_reader = csv.DictReader(students_file)

for row in csv_reader:

    print(row)
```

Returns

```python
{
'name':'Alice',
'department':'Computer Science'
}
```

---

# CSV Writer

```python
csv_writer = csv.writer(students_file)

csv_writer.writerows(students_lol)
```

Writes multiple rows into a CSV file.

---

## 📊 CSV Flow Diagram

```text
CSV File

↓

Open

↓

csv.reader()

↓

Read Rows

↓

Print
```

---

# 🌍 Real World Examples

* Student Management System
* Employee Payroll
* Banking Transactions
* Sales Reports
* Attendance System
* Data Analysis

---

# 💡 Best Practices

* Always use `with open()`.
* Close files if not using `with`.
* Use `DictReader` for meaningful column names.
* Use binary mode (`rb`) for images and PDFs.
* Handle exceptions when working with files.

---

# 🎤 Interview Questions

### 1. What is the datetime module?

It is a built-in Python module used to work with dates and times.

---

### 2. What does `strftime()` do?

Formats a date and time into a readable string.

---

### 3. Difference between `write()` and `writelines()`?

| `write()`         | `writelines()`          |
| ----------------- | ----------------------- |
| Writes one string | Writes multiple strings |

---

### 4. Why use `with open()`?

It automatically closes the file after use.

---

### 5. Difference between `csv.reader()` and `csv.DictReader()`?

| `csv.reader()` | `csv.DictReader()`   |
| -------------- | -------------------- |
| Returns a list | Returns a dictionary |

---

### 6. What is binary mode?

Binary mode (`rb`, `wb`) is used to read or write non-text files such as images, videos, PDFs, and audio.

---

# 📌 Key Points to Remember

* `datetime.now()` → Current date and time
* `strftime()` → Format date and time
* `open()` → Open a file
* `read()`, `readlines()` → Read file contents
* `write()` → Write text
* `writelines()` → Write multiple lines
* `with open()` → Automatically closes the file
* `csv.reader()` → Reads CSV rows as lists
* `csv.DictReader()` → Reads CSV rows as dictionaries
* `csv.writer()` → Writes CSV data

---

# 📋 Final Summary

| Topic              | Purpose                    |
| ------------------ | -------------------------- |
| `datetime`         | Work with date and time    |
| `strftime()`       | Format date and time       |
| `open()`           | Open a file                |
| `readlines()`      | Read all lines into a list |
| `write()`          | Write text to a file       |
| `writelines()`     | Write multiple strings     |
| `with open()`      | Safe file handling         |
| `csv.reader()`     | Read CSV as lists          |
| `csv.DictReader()` | Read CSV as dictionaries   |
| `csv.writer()`     | Write data to CSV          |

This structure matches the style of your previous notes and is ready to use as a professional Canva or GitHub README chapter.
