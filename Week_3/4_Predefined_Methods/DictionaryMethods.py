# ===========================================
# DICTIONARY METHODS
# ===========================================
# 1. Create Dictionary
student = {
    "id": 101,
    "name": "Ramesh",
    "course": "Python",
    "city": "Hyderabad"
}

print(student)

# 2. Access Value using Key
print(student["name"])

# 3. get()
print(student.get("course"))

# 4. keys()
print(student.keys())

# 5. values()
print(student.values())

# 6. items()
print(student.items())

# 7. Add New Key
student["email"] = "ramesh@gmail.com"
print(student)

# 8. Update Value
student["city"]  = "Bangalore"
print(student)

# 9. update()
student.update({
    "course": "Full Stack Python",
    "mobile": "9876543210"
})

print(student)

# 10. pop()
student.pop("mobile")
print(student)

# 11. popitem()
student.popitem()
print(student)

# 12. setdefault()
student.setdefault("country", "India")
print(student)

# 13. copy()
student_copy = student.copy()
print(student_copy)

# 14. clear()
demo = {
    "a": 10,
    "b": 20
}

demo.clear()
print(demo)

# 15. len()
print(len(student))

# 16. Membership
print("name" in student)
print("salary" in student)

# 17. Iterate Keys
for key in student:
    print(key)

# 18. Iterate Values
for value in student.values():
    print(value)

# 19. Iterate Items
for key, value in student.items():
    print(key, value)