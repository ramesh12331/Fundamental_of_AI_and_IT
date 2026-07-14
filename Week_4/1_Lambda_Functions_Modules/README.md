# 🐍 Python Lambda Functions, map(), filter(), reduce() & Modules

> A beginner-friendly guide with definitions, syntax, examples, interview questions, and summary.

---

# 📚 Table of Contents

1. Lambda Function
2. map()
3. filter()
4. reduce()
5. Modules
6. Types of Modules
7. Popular Third-Party Modules
8. Interview Questions & Answers
9. Final Summary

---

# 🚀 Lambda Function

## Definition

A **Lambda Function** is a small anonymous function in Python.

- Anonymous means **it has no function name**.
- It can have **any number of arguments**.
- It can contain **only one expression**.
- The result of the expression is automatically returned.

---

## Syntax

```python
variable_name = lambda arguments: expression
```

---

## Example 1

```python
square = lambda x: x * x

print(square(5))
```

### Output

```
25
```

### Explanation

```
lambda x: x * x

x = 5

5 × 5 = 25
```

---

## Example 2

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```
30
```

---

## Example 3

```python
greeting = lambda name: "Hello " + name

print(greeting("Ramesh"))
```

### Output

```
Hello Ramesh
```

---

# 🗺️ map()

## Definition

The **map()** function applies a function to **every element** in an iterable.

It returns a **map object**, so we usually convert it into a list.

---

## Syntax

```python
list(
    map(function, iterable)
)
```

Using Lambda

```python
list(
    map(lambda arguments: expression, iterable)
)
```

---

## Example 1

```python
numbers = [1, 2, 3, 4, 5]

square = list(
    map(lambda x: x * x, numbers)
)

print(square)
```

### Output

```
[1, 4, 9, 16, 25]
```

---

### Step-by-Step

```
1 × 1 = 1
2 × 2 = 4
3 × 3 = 9
4 × 4 = 16
5 × 5 = 25
```

---

## Example 2

```python
prices = [100, 200, 300]

gst = list(
    map(lambda price: price + price * 0.18, prices)
)

print(gst)
```

### Output

```
[118.0, 236.0, 354.0]
```

---

# 🔍 filter()

## Definition

The **filter()** function returns only the elements that satisfy a condition.

---

## Syntax

```python
list(
    filter(function, iterable)
)
```

Using Lambda

```python
list(
    filter(lambda arguments: expression, iterable)
)
```

---

## Example 1

```python
numbers = [10, 15, 20, 25, 30]

even = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even)
```

### Output

```
[10, 20, 30]
```

---

### Explanation

```
10 ✔
15 ✘
20 ✔
25 ✘
30 ✔
```

---

## Example 2

```python
marks = [35, 80, 25, 90, 60]

passed = list(
    filter(lambda mark: mark >= 35, marks)
)

print(passed)
```

### Output

```
[35, 80, 90, 60]
```

---

# ➕ reduce()

## Definition

The **reduce()** function reduces all elements into a **single value**.

It is available inside the **functools** module.

---

## Import

```python
from functools import reduce
```

---

## Syntax

```python
reduce(
    lambda accumulator, current: expression,
    iterable
)
```

With Initial Value

```python
reduce(
    lambda accumulator, current: expression,
    iterable,
    initial_value
)
```

---

## Example 1

```python
from functools import reduce

numbers = [9, 6, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)
```

### Output

```
20
```

---

### Dry Run

```
9 + 6 = 15

15 + 5 = 20

Answer = 20
```

---

## Example 2

```python
from functools import reduce

numbers = [2, 3, 4]

product = reduce(
    lambda a, b: a * b,
    numbers
)

print(product)
```

### Output

```
24
```

---

### Dry Run

```
2 × 3 = 6

6 × 4 = 24
```

---

# 👨‍🏫 Example Explained in Class

```python
a = [9, 6, 5]

sum = 0

sum = sum + a[0]
sum = sum + a[1]
sum = sum + a[2]

print(sum)
```

### Output

```
20
```

---

### Step-by-Step

Initially

```
sum = 0
```

After first line

```
sum = 0 + 9

sum = 9
```

After second line

```
sum = 9 + 6

sum = 15
```

After third line

```
sum = 15 + 5

sum = 20
```

Final Output

```
20
```

---

# 📦 Module

## Definition

A **Module** is a Python file (.py) that contains reusable code such as:

- Functions
- Variables
- Classes

Modules help us avoid writing the same code again and again.

---

## Why Use Modules?

✅ Reuse code

✅ Save development time

✅ Better organization

✅ Easy maintenance

---

## Syntax

Import Entire Module

```python
import module_name
```

Example

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

Import Specific Function

```python
from math import sqrt

print(sqrt(49))
```

Output

```
7.0
```

---

Import Everything

```python
from math import *
```

---

Rename Module

```python
import math as m

print(m.pi)
```

---

# 📂 Types of Modules

## 1. User-defined Module

Created by the programmer.

Example

```
calculator.py
```

```python
def add(a, b):
    return a + b
```

Use

```python
import calculator

print(calculator.add(10,20))
```

Output

```
30
```

---

## 2. Built-in Module

Already available in Python.

Examples

```
math

random

datetime

os

sys

statistics

functools
```

---

## 3. Third-party Module

Installed using pip.

```
pip install package_name
```

Example

```
pip install pandas
```

---

# 🌟 Popular Third-Party Modules

| Module | Purpose |
|---------|---------|
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Charts |
| Plotly | Interactive Charts |
| OpenCV | Computer Vision |
| TensorFlow | Deep Learning |
| PyTorch | Machine Learning |
| Scikit-learn | Machine Learning Algorithms |
| Requests | HTTP Requests |
| BeautifulSoup | Web Scraping |
| Flask | Web Development |
| Django | Full Stack Web Framework |
| FastAPI | High Performance APIs |

---

# 🔥 Difference Between map(), filter(), reduce()

| Feature | map() | filter() | reduce() |
|----------|--------|-----------|-----------|
| Purpose | Transform Data | Filter Data | Reduce Data |
| Output | Iterable | Iterable | Single Value |
| Condition | No | Yes | No |
| Returns | Modified Elements | Matching Elements | One Result |

---

# 🎯 Real-Life Examples

## map()

Increase every employee salary by 10%.

---

## filter()

Find students who passed the exam.

---

## reduce()

Calculate total shopping bill.

---

# 💼 Interview Questions & Answers

## 1. What is Lambda Function?

Answer:

A lambda function is a small anonymous function with only one expression.

---

## 2. Why use Lambda?

Answer:

To write short and simple functions without using def.

---

## 3. Can Lambda have multiple statements?

Answer:

No.

It can contain only one expression.

---

## 4. What is map()?

Answer:

map() applies a function to every element of an iterable.

---

## 5. What is filter()?

Answer:

filter() returns only elements that satisfy a condition.

---

## 6. What is reduce()?

Answer:

reduce() combines all elements into a single value.

---

## 7. Which module contains reduce()?

Answer:

functools

---

## 8. What is a Module?

Answer:

A module is a Python file containing reusable code.

---

## 9. Difference between User-defined and Built-in Module?

Answer

User-defined

Created by programmer.

Built-in

Already available in Python.

---

## 10. How do you install third-party modules?

Answer

```
pip install module_name
```

Example

```
pip install pandas
```

---

## 11. Difference between Lambda and def?

| Lambda | def |
|----------|------|
| Anonymous | Named Function |
| One Expression | Multiple Statements |
| Short Code | Large Code |

---

## 12. What does map() return?

Answer

A map object.

Usually converted into a list.

---

## 13. What does filter() return?

Answer

Only elements that satisfy the condition.

---

## 14. Does reduce() return a list?

Answer

No.

It returns a single value.

---

## 15. Can Lambda accept multiple arguments?

Answer

Yes.

Example

```python
multiply = lambda a, b: a * b

print(multiply(5, 6))
```

Output

```
30
```

---

# 📝 Final Summary

✅ Lambda is a small anonymous function.

✅ map() transforms every element.

✅ filter() selects matching elements.

✅ reduce() combines elements into one value.

✅ Modules help organize and reuse code.

✅ Python modules are of three types:
- User-defined
- Built-in
- Third-party

✅ Popular libraries include:
- NumPy
- Pandas
- Matplotlib
- TensorFlow
- Django
- Flask
- FastAPI

Master these concepts to write cleaner, shorter, and more efficient Python programs.