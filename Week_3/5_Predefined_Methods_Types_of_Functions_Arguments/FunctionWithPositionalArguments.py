# ============================================
# FUNCTION WITH POSITIONAL ARGUMENTS
# ============================================
def grocery_order(customer_name, item, quantity, price):
    total_amount = price * quantity

    print(f"Customer Name : {customer_name}")
    print(f"Item : {item}")
    print(f"Quantity : {quantity}")
    print(f"Price : {price}")
    print(f"Total Amount : {total_amount}")

grocery_order("Karthik", "Onions", 1, 30)

# ============================================
# DEFAULT ARGUMENTS
# ============================================
def grocery_order(customer_name, item, quantity = 1, price = 0):
    total_amount = quantity*price

    print(f"Customer Name : {customer_name}")
    print(f"Item : {item}")
    print(f"Quantity : {quantity}")
    print(f"Price : {price}")
    print(f"Total Amount : {total_amount}")

print("DEFAULT ARGUMENTS")
grocery_order("Karthik", "Onions")
grocery_order("Karthik", "Onions", 2)

# ============================================
# KEYWORD ARGUMENTS
# ============================================

def enroll_student(name, course, duration, fee):
    print(f"Student Name : {name}")
    print(f"Course : {course}")
    print(f"Duration : {duration}")
    print(f"Fee : {fee}")

print("KEYWORD ARGUMENTS")
enroll_student(course="AI/ML", duration="4 Months", fee=50000, name="Karthik")

# ============================================
# *ARGS
# ============================================

def calculate_total(customer_name, *item_price):
    total_amount = sum(item_price)

    print(item_price)
    print(f"Customer Name : {customer_name}")
    print(f"Total Amount : {total_amount}")

print("*ARGS")
calculate_total("Karthik", 100, 200, 300)
calculate_total("Karthik", 100, 200, 300, 400, 500)

# ============================================
# **KWARGS
# ============================================
def register_student(student_name, **student_details):
    print(student_details)
    print(f"Student Name : {student_name}")

print("**KWARGS")
register_student("Naveen", course="AI/ML", duration="4 Months", fee=50000)