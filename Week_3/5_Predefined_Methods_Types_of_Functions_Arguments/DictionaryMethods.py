# =====================================
# Dictionary Methods
# =====================================

employee = {
    "id": "EMP001",
    "name": "Alice Johnson",
    "age": 30,
    "department": "Engineering",
    "position": "Senior Developer",
    "salary": 95000,
    "email": "alice.johnson@company.com",
    "phone": "+1-555-0101",
    "hire_date": "2021-03-15"
}

# keys()
print("Dictionary Keys")
print(employee.keys())

# values()
print("\nDictionary Values")
print(employee.values())

# items()
print("\nDictionary Items")
print(employee.items())

# Loop through dictionary
print("\nEmployee Details")
for key, value in employee.items():
    print(f"{key} : {value}")

# get()
print("\nEmployee Name")
print(employee.get("name", ""))
print(employee.get("first_name", "abc")) #print default value

# update()
employee_additional_details = {
    "skills": ["Python", "Django", "PostgreSQL", "Docker"],
    "is_active": True,
    "manager_id": "EMP005",
    "address": {
        "street": "123 Main St",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94105"
    }
}

employee.update(employee_additional_details)
print("\nUpdated Employee")
print(employee)

# ============================================
# dict.pop(key, default)
# Removes the key and returns its value.
# If the key is not found, returns the default value.
# ============================================
student = {
    "name": "Ramesh",
    "age": 22,
    "course": "Python"
}

removed_value = student.pop("age", "Key Not Found")
print("Removed Value:", removed_value)
print("Dictionary:", student)

# ============================================
# dict.clear()
# Removes all key-value pairs from the dictionary.
# ============================================
student = {
    "name": "Ramesh",
    "age": 22,
    "course": "Python"
}

student.clear()
print(student)

# ============================================
# dict.copy()
# Returns a shallow copy of the dictionary.
# ============================================

student = {
    "name": "Ramesh",
    "age": 22
}

student_copy = student.copy()
print("Original Dictionary:", student)
print("Copied Dictionary:", student_copy)

# ============================================
# dict.fromkeys(iterable, value)
# Creates a new dictionary with given keys
# and assigns the same value to each key.
# ============================================
subjects = ["Python", "Java", "C++"]

marks = dict.fromkeys(subjects, 0)
print(marks)