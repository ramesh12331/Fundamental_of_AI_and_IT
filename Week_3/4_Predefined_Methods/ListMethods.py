# ===========================================
# LIST METHODS
# ===========================================

# -------------------------------------------
# 1. Create a List
# -------------------------------------------

cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Delhi"
]

print(cities)

# -------------------------------------------
# 2. append()
# -------------------------------------------

cities.append("Vizaz")
print(cities)

# -------------------------------------------
# 3. append() Again
# -------------------------------------------
cities.append("Kolkata")
print(cities)

# -------------------------------------------
# 4. extend()
# -------------------------------------------
adjectives = [
    "Epic",
    "Silent",
    "Quantum",
    "Frosty",
    "Cosmic",
    "Golden"
]

nouns = [
    "Ninja",
    "Panda",
    "Wizard",
    "Falcon",
    "Cyborg",
    "Phoenix"
]

adjectives.extend(nouns)
print(adjectives)

# -------------------------------------------
# 5. insert()
# -------------------------------------------
languages = [
    "Python",
    "Java",
    "JavaScript",
    "C++"
]

languages.insert(2, "Go")
print(languages)

# -------------------------------------------
# 6. pop()
# -------------------------------------------
adjectives.pop(4)
print(adjectives)

# -------------------------------------------
# 7. pop() First Element
# -------------------------------------------
adjectives.pop(0)
print(adjectives)

# -------------------------------------------
# 8. remove()
# -------------------------------------------
adjectives.remove("Falcon")
print(adjectives)

# -------------------------------------------
# 9. clear()
# -------------------------------------------
numbers = [10, 20, 30, 40]
numbers.clear()
print(numbers)

# -------------------------------------------
# 10. index()
# -------------------------------------------

languages = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "Go",
    "Rust",
    "Ruby"
]

print(languages.index("Ruby"))

# -------------------------------------------
# 11. count()
# -------------------------------------------
languages = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Python",
    "Go"
]

print(languages.count("Python"))

# -------------------------------------------
# 12. sort()
# -------------------------------------------
languages = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "C#",
    "Go",
    "Rust",
    "Ruby"
]
languages.sort()
print(languages)

# -------------------------------------------
# 13. sort(reverse=True)
# -------------------------------------------
languages.sort(reverse=True)
print(languages)

# -------------------------------------------
# 14. reverse()
# -------------------------------------------
languages.reverse()
print(languages)

# -------------------------------------------
# 15. reverse() Cities
# -------------------------------------------
cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Delhi"
]

cities.reverse()
print(cities)

# -------------------------------------------
# 16. copy()
# -------------------------------------------
copied_cities = cities.copy()
print(copied_cities)

# -------------------------------------------
# 17. join()
# -------------------------------------------
name_list = [
    "Keerthi",
    "Palagala"
]

print(" ".join(name_list))
print("_".join(name_list))

# -------------------------------------------
# 18. split()
# -------------------------------------------
student_name = "Keerthi Palagala"
print(student_name.split())

# -------------------------------------------
# 19. strip()
# -------------------------------------------
student_name = "     Keerthi Palagala     "
print(student_name.strip())

# -------------------------------------------
# 20. len()
# -------------------------------------------

print(len(cities))

# -------------------------------------------
# 21. max()
# -------------------------------------------
numbers = [10, 40, 25, 80, 15]
print(max(numbers))

# -------------------------------------------
# 22. min()
# -------------------------------------------
print(min(numbers))

# -------------------------------------------
# 23. sum()
# -------------------------------------------

print(sum(numbers))