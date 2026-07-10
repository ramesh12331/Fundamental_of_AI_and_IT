# ===========================================
# BUILT-IN FUNCTIONS & LIST COMPREHENSION
# ===========================================

# -------------------------------------------
# 1. sum()
# -------------------------------------------
subject_marks = [90, 45, 67]
print(sum(subject_marks))

# -------------------------------------------
# 2. List of Users (Dictionary)
# -------------------------------------------
users = [
    {
        "id": 1,
        "name": "Robert Smith",
        "email": "robert.smith@example.com",
        "role": "User",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Maria Garcia",
        "email": "mgarcia@example.net",
        "role": "Admin",
        "is_active": False
    },
    {
        "id": 3,
        "name": "James Wilson",
        "email": "jwilson@example.org",
        "role": "Manager",
        "is_active": True
    }
]

print(users)

# -------------------------------------------
# 3. List Comprehension
# Get Active Status
# -------------------------------------------
active_users = [
    user["is_active"]
    for user in users
    if user["is_active"] == True
]

print(active_users)

# -------------------------------------------
# 4. Active User Records
# -------------------------------------------
active_users = [
    user
    for user in users
    if user["is_active"] == True
]

print(active_users)

# -------------------------------------------
# 5. Cities List
# -------------------------------------------
cities = [
    "Kolkata",
    "Vizag",
    "Delhi",
    "Mumbai",
    "Ahmedabad",
    "Chennai",
    "Jaipur",
    "Bengaluru",
    "Hyderabad"
]

print(cities)

# -------------------------------------------
# 6. Convert Cities to Uppercase
# -------------------------------------------
formatted_cities = [
    city.upper()
    for city in cities
]

print(formatted_cities)

# -------------------------------------------
# 7. Even Numbers using List Comprehension
# -------------------------------------------
numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = [
    number
    for number in numbers
    if number%2 == 0
]
print(even_numbers)

# -------------------------------------------
# 8. Odd Numbers using List Comprehension
# -------------------------------------------

odd_numbers = [
    number
    for number in numbers
    if number%2 != 0
]
print(odd_numbers)

# -------------------------------------------
# 9. Squares of Numbers
# -------------------------------------------

square_numbers = [
    number ** 2
    for number in numbers
]
print(square_numbers)

# -------------------------------------------
# 10. Uppercase Names
# -------------------------------------------
names = [
    "ramesh",
    "mahesh",
    "suresh",
    "ganesh"
]

upper_names = [
    name.upper()
    for name in names
]

print(upper_names)

# -------------------------------------------
# 11. Length of Each Name
# -------------------------------------------
name_lengths = [
    len(name)
    for name in names
]

print(name_lengths)

# -------------------------------------------
# 12. List of Days
# -------------------------------------------
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print(days)

# -------------------------------------------
# 13. Convert List to Tuple
# -------------------------------------------
print(tuple(days))

# -------------------------------------------
# 14. Convert String to Tuple
# -------------------------------------------
print(tuple("Monday"))

# -------------------------------------------
# 15. Find Index
# -------------------------------------------
print(days.index("Wednesday"))

# -------------------------------------------
# 16. Length of List
# -------------------------------------------
print(len(days))

# -------------------------------------------
# 17. Maximum Value
# -------------------------------------------
nums = (5, 8, 9, 4, 4)
print(max(nums))

# -------------------------------------------
# 18. Minimum Value
# -------------------------------------------

print(min(nums))

# -------------------------------------------
# 19. Sum of Tuple
# -------------------------------------------
print(sum(nums))