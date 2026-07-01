# 🎓 Python Mini Projects
## Beginner Function-Based Projects

A collection of beginner-friendly Python mini projects designed to improve problem-solving skills using **functions**, **conditional statements**, and **return values**.

---

# 📚 Projects Included

- 🎓 Student Result Management System
- 🎬 Movie Ticket Booking System

---

# 🎯 Learning Objectives

After completing these projects, you will be able to:

- Create reusable functions
- Pass arguments to functions
- Return values from functions
- Use if-elif-else conditions
- Solve real-world programming problems
- Write clean and modular Python code

---

# 🎓 Mini Project 1
# Student Result Management System

## 📖 Introduction

The Student Result Management System calculates a student's:

- Total Marks
- Average
- Grade
- Pass/Fail Status

This project demonstrates how functions work together to solve a real-world problem.

---

# 📌 Problem Statement

Create functions to:

- Calculate Total Marks
- Calculate Average
- Assign Grade
- Determine Pass/Fail

---

# 📥 Input

| Subject | Marks |
|---------|------:|
| Maths | 85 |
| Science | 78 |
| English | 92 |
| Social | 74 |
| Computer | 88 |

---

# 📤 Output

```text
Total Marks : 417
Average     : 83.4
Grade       : A
Result      : Pass
```

---

# 🧠 Step 1: Analyze the Problem

### Inputs

- Maths
- Science
- English
- Social
- Computer

### Processing

```
Input Marks
      ↓
Calculate Total
      ↓
Calculate Average
      ↓
Assign Grade
      ↓
Determine Result
```

### Outputs

- Total Marks
- Average
- Grade
- Result

---

# 🛠 Required Functions

| Function | Purpose |
|-----------|---------|
| calculate_total() | Calculates total marks |
| calculate_average() | Calculates average |
| assign_grade() | Assigns grade |
| determine_result() | Checks Pass/Fail |

---

# 🧩 Step 2: Break the Problem

```
Input Marks
      ↓
Calculate Total
      ↓
Calculate Average
      ↓
Assign Grade
      ↓
Determine Result
      ↓
Display Report
```

---

# 💻 Python Code

```python
def calculate_total(maths, science, english, social, computer):
    return maths + science + english + social + computer


def calculate_average(total):
    return total / 5


def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def determine_result(avg):
    if avg >= 35:
        return "Pass"
    else:
        return "Fail"


maths = 85
science = 78
english = 92
social = 74
computer = 88

total = calculate_total(maths, science, english, social, computer)
average = calculate_average(total)
grade = assign_grade(average)
result = determine_result(average)

print("Total Marks :", total)
print("Average     :", average)
print("Grade       :", grade)
print("Result      :", result)
```

---

# 🔍 Dry Run

| Step | Value |
|------|------:|
| Maths | 85 |
| Science | 78 |
| English | 92 |
| Social | 74 |
| Computer | 88 |
| Total | 417 |
| Average | 83.4 |
| Grade | A |
| Result | Pass |

---

# 📊 Flow Diagram

```text
Start
  │
  ▼
Input Marks
  │
  ▼
Calculate Total
  │
  ▼
Calculate Average
  │
  ▼
Assign Grade
  │
  ▼
Determine Result
  │
  ▼
Display Report
  │
  ▼
End
```

---

# 🌍 Real-World Applications

- School Management Systems
- College Result Portals
- Online Examination Systems

---

# 🎤 Interview Question

### Why do we create separate functions?

Each function performs one specific task.

Benefits:

- Easy to understand
- Easy to reuse
- Easy to test
- Easy to maintain

---

# 🎬 Mini Project 2
# Movie Ticket Booking System

## 📖 Introduction

A beginner-friendly ticket booking project that uses functions to simulate movie ticket booking.

---

# 📌 Problem Statement

Create functions to:

- Select Movie
- Choose Seats
- Calculate Ticket Price
- Confirm Booking

---

# 🧠 Step 1: Analyze the Problem

### Inputs

- Movie Name
- Number of Seats

### Outputs

- Movie
- Seats
- Total Price
- Booking Confirmation

---

# 🛠 Required Functions

| Function | Purpose |
|-----------|---------|
| select_movie() | Select movie |
| choose_seats() | Choose seats |
| calculate_ticket_price() | Calculate total bill |
| confirm_booking() | Display booking details |

---

# 🧩 Step 2: Break the Problem

```text
Select Movie
      ↓
Choose Seats
      ↓
Calculate Ticket Price
      ↓
Confirm Booking
```

---

# 💻 Python Code

```python
def select_movie(movie):
    return movie


def choose_seats(seats):
    return seats


def calculate_ticket_price(seats):
    ticket_price = 200
    return seats * ticket_price


def confirm_booking(movie, seats, total):
    print("\nBooking Confirmed")
    print("------------------")
    print("Movie :", movie)
    print("Seats :", seats)
    print("Total :", total)


movie = select_movie("Rocket Tree")
seats = choose_seats(3)
total = calculate_ticket_price(seats)

confirm_booking(movie, seats, total)
```

---

# 🔍 Dry Run

| Step | Value |
|------|-------|
| Movie | Rocket Tree |
| Seats | 3 |
| Ticket Price | ₹200 |
| Total Price | ₹600 |

---

# 📊 Flow Diagram

```text
Start
  │
  ▼
Select Movie
  │
  ▼
Choose Seats
  │
  ▼
Calculate Ticket Price
  │
  ▼
Confirm Booking
  │
  ▼
Print Ticket
  │
  ▼
End
```

---

# 🌍 Real-World Applications

- BookMyShow
- PVR Cinemas
- INOX
- Multiplex Booking Systems

---

# 💡 Problem-Solving Strategy

Follow these six steps for every Python project:

1. Read the problem carefully.
2. Identify the inputs.
3. Identify the outputs.
4. Break the problem into small tasks.
5. Create one function for each task.
6. Call the functions in the correct order and use returned values.

---

# 🎯 Skills Practiced

- Python Functions
- Parameters
- Return Statements
- Conditional Statements
- Variables
- Program Flow
- Problem Solving
- Modular Programming

---

# 🚀 Future Improvements

- User input support
- Exception handling
- Loops and menus
- File handling
- Database integration
- GUI using Tkinter
- Web version using Flask

---

# 👨‍💻 Author

**Python Mini Projects**

Made for beginners to practice Python programming and build strong problem-solving skills.

⭐ Happy Coding!