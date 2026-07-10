# ===========================================
# STRING METHODS
# ===========================================

# -------------------------------------------
# 1. upper()
# -------------------------------------------

announcement = "The office will remain closed on Friday due to maintenance."
print(announcement.upper())

# -------------------------------------------
# 2. lower()
# -------------------------------------------
print(announcement.lower())

# -------------------------------------------
# 3. capitalize()
# -------------------------------------------
name = "hari krishna"
print(name.capitalize())

# -------------------------------------------
# 4. title()
# -------------------------------------------
print(name.title())

# -------------------------------------------
# 5. swapcase()
# -------------------------------------------

announcement = "The Office Will Remain Closed"
print(announcement.swapcase())

# -------------------------------------------
# 6. isalpha()
# -------------------------------------------
name = "AmitabhBachan"
print(name.isalpha())

# -------------------------------------------
# 7. isdigit()
# -------------------------------------------
aadhar = "985689002345A"
print(aadhar.isdigit())

# -------------------------------------------
# 8. isalnum()
# -------------------------------------------
pan_no = "ABCDE1234F"
print(pan_no.isalnum())

# -------------------------------------------
# 9. isspace()
# -------------------------------------------
address = "  Hyderabad"
print("is space: ",address.isspace())

# -------------------------------------------
# 10. startswith()
# -------------------------------------------
company_address = "https://datavalley.ai"
print(company_address.startswith("https://"))

# -------------------------------------------
# 11. endswith()
# -------------------------------------------
print(company_address.endswith(".ai"))

# -------------------------------------------
# 12. find()
# -------------------------------------------
address = "123 MG Road, Hyderabad, Telangana, India"
print(address.find("Pune"))
print(address.find("Hyderabad"))

# index() with Exception Handling

try:
    print(address.index("Pune"))
except ValueError:
    print("Substring not found")

# -------------------------------------------
# 14. count()
# -------------------------------------------
article = "India is in South Asia. India is a democratic country."
print(article.count("India"))

# -------------------------------------------
# 15. replace()
# -------------------------------------------

article = "India is a beautiful country."
print(article.replace("India", "Bharat"))

# -------------------------------------------
# 16. split()
# -------------------------------------------
student_name = "Keerthi Palagala"
print(student_name.split())

# -------------------------------------------
# 17. join()
# -------------------------------------------

name_list = ["Keerthi", "Palagala"]
print(" ".join(name_list))
print(", ".join(name_list))

# -------------------------------------------
# 18. list()
# -------------------------------------------
mobile = "9032345245"
print(list(mobile))