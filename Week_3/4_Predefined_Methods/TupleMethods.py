# ===========================================
# TUPLE METHODS
# ===========================================

# -------------------------------------------
# 1. Create a Tuple
# -------------------------------------------

days_tuple = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days_tuple)

# -------------------------------------------
# 2. Access First Element
# -------------------------------------------

first_day = days_tuple[0]
print(first_day)

# -------------------------------------------
# 3. Access Second Element
# -------------------------------------------
second_day = days_tuple[1]
print(second_day)

# -------------------------------------------
# 4. Access Last Element
# -------------------------------------------
last_day = days_tuple[-1]
print(last_day)

# -------------------------------------------
# 5. Tuple Slicing
# -------------------------------------------
print(days_tuple[0:3])
print(days_tuple[2:6])
print(days_tuple[:4])
print(days_tuple[4:])
print(days_tuple[::-1])

# -------------------------------------------
# 6. Tuple Packing
# -------------------------------------------
student = (
    101,
    "Ramesh",
    "Python"
)

print(student)

# -------------------------------------------
# 7. Tuple Unpacking
# -------------------------------------------
student_id, student_name, course = student

print(student_id)
print(student_name)
print(course)

# -------------------------------------------
# 8. Tuple Unpacking (Days)
# -------------------------------------------
first, second, third, fourth, fifth, sixth, seventh = days_tuple

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)

# -------------------------------------------
# 9. count()
# -------------------------------------------
numbers = (10, 20, 30, 20, 40, 20, 50)

print(numbers.count(20))

# -------------------------------------------
# 10. index()
# -------------------------------------------
print(numbers.index(40))

# -------------------------------------------
# 11. len()
# -------------------------------------------
print(len(numbers))

# -------------------------------------------
# 12. max()
# -------------------------------------------
print(max(numbers))

# -------------------------------------------
# 13. min()
# -------------------------------------------
print(min(numbers))

# -------------------------------------------
# 14. sum()
# -------------------------------------------
print(sum(numbers))

# -------------------------------------------
# 15. Membership Operator
# -------------------------------------------

print("Monday" in days_tuple)
print("Sunday" in days_tuple)
print("Holiday" in days_tuple)

# -------------------------------------------
# 16. Iterate Using for Loop
# -------------------------------------------

for day in days_tuple:
    print(day)

# -------------------------------------------
# 17. Enumerate Tuple
# -------------------------------------------
for index, day in enumerate(days_tuple):
    print(index, day)

# -------------------------------------------
# 18. Tuple of User Roles
# -------------------------------------------
user_roles = [
    (1, "Admin"),
    (2, "Editor"),
    (3, "Viewer"),
    (4, "Guest")
]

print(user_roles)

# -------------------------------------------
# 19. Access Tuple Values Using Index
# -------------------------------------------
for role_id, role_name in user_roles:
    print(role_id, role_name)

# -------------------------------------------
# 20. Tuple Unpacking in Loop
# -------------------------------------------
for role_id, role_name in user_roles:
    print(role_id, role_name)

# -------------------------------------------
# 21. Nested Tuple
# -------------------------------------------
employee = (
    101,
    "Ramesh",
    (
        "Python",
        "Java",
        "React"
    )
)

print(employee)
print(employee[2])
print(employee[2][0])
print(employee[2][1])
print(employee[2][2])

# -------------------------------------------
# 22. Tuple Concatenation
# -------------------------------------------
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)

# -------------------------------------------
# 23. Tuple Repetition
# -------------------------------------------
print(("Python",)*5)

# -------------------------------------------
# 24. Convert List to Tuple
# -------------------------------------------
cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai"
]
cities_tuple = tuple(cities)
print(cities_tuple) 

# -------------------------------------------
# 25. Convert String to Tuple
# -------------------------------------------
word = "Python"
print(tuple(word))