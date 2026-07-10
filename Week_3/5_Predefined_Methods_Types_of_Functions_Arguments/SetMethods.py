# =====================================
# Set Methods
# =====================================

courses_list = {
    "Python Programming",
    "Data Structures & Algorithms",
    "Web Development with Django",
    "Machine Learning",
    "Cloud Computing with AWS",
    "DevOps & CI/CD",
    "Cybersecurity Fundamentals"
}

courses_list.add("Database Management")
print(courses_list)

# remove()
courses_list.remove("Database Management")
# print(courses_list)

# discard()
courses_list.discard("Database Management")
print(courses_list)

# pop()
courses_list.pop()
print(courses_list)

# clear()
courses_list.clear()
print(courses_list)

# ============================================
# Set Example: union() and intersection()
# ============================================

# Data Science Technologies
ds_technologies = {
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Tableau"
}

# Artificial Intelligence Technologies
ai_technologies = {
    "Python",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "OpenCV"
}

# --------------------------------------------
# union()
# Combines all unique elements from both sets.
# --------------------------------------------

print("Union:")
print(ds_technologies.union(ai_technologies))

# --------------------------------------------
# intersection()
# Returns only the common elements.
# --------------------------------------------

print("\nIntersection:")
print(ds_technologies.intersection(ai_technologies))

# ============================================
# FROZENSET OPERATIONS
# ============================================

technologies = frozenset([
    "Keras",
    "OpenCV",
    "Stable Diffusion",
    "AutoGen"
])

technologies2 = frozenset([
    "Jupyter Notebook",
    "Power BI",
    "Apache Kafka",
    "Scikit-learn"
])

print("FROZENSET OPERATIONS")
print(technologies.intersection(technologies2))
print(technologies.difference(technologies2))
print(technologies.symmetric_difference(technologies2))