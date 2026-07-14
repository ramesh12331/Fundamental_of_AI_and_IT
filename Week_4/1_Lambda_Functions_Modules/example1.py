# ============================================================
# Lambda Functions, map(), filter(), and reduce() — Examples
# ============================================================


# ------------------------------------------------------------
# 1. Basic Lambda Function
# ------------------------------------------------------------
# Lambda Function
apply_gst = lambda price: price + (price * 18 / 100)

apply_gst(100)
# Output: 118.0

print(apply_gst(100))
# Output: 118.0

print(apply_gst(100))
print(apply_gst(4000))
print(apply_gst(500))
# Output:
# 118.0
# 4720.0
# 590.0


# ------------------------------------------------------------
# 2. map() — Capitalize a list of usernames
# ------------------------------------------------------------
users = ['amardeep', 'jyothi', 'pradeep', 'nagarjuna']

modified_users = list(map(lambda user: user.title(), users))
modified_users
# Output: ['Amardeep', 'Jyothi', 'Pradeep', 'Nagarjuna']


# ------------------------------------------------------------
# 3. map() — Apply a 10% discount to a shopping cart
# ------------------------------------------------------------
cart = [
    ('T-Shirt', 1500),
    ('Jeans', 2500),
    ('Perfume', 580),
    ('Watch', 5000)
]

discounted_cart = list(map(lambda product: (product[0], product[1] - product[1] * 0.1), cart))
discounted_cart
# Output: [('T-Shirt', 1350.0), ('Jeans', 2250.0), ('Perfume', 522.0), ('Watch', 4500.0)]


# ------------------------------------------------------------
# 4. Sample Dataset — Courses
# ------------------------------------------------------------
courses = [
    {
        "id": "CS101",
        "title": "Python Programming",
        "instructor": "Dr. Alice Brown",
        "department": "Computer Science",
        "duration_weeks": 8,
        "credits": 3,
        "level": "Beginner",
        "price": 199.99,
        "rating": 4.8,
        "enrolled_students": 1200,
        "is_active": True,
        "tags": ["python", "programming", "beginner"],
        "schedule": {"day": "Monday", "time": "10:00 AM"}
    },
    {
        "id": "CS102",
        "title": "Data Structures & Algorithms",
        "instructor": "Prof. John Smith",
        "department": "Computer Science",
        "duration_weeks": 12,
        "credits": 4,
        "level": "Intermediate",
        "price": 249.99,
        "rating": 4.6,
        "enrolled_students": 980,
        "is_active": True,
        "tags": ["algorithms", "data structures", "problem solving"],
        "schedule": {"day": "Wednesday", "time": "2:00 PM"}
    },
    {
        "id": "WD201",
        "title": "Web Development with Django",
        "instructor": "Ms. Carol White",
        "department": "Web Technologies",
        "duration_weeks": 10,
        "credits": 3,
        "level": "Intermediate",
        "price": 229.99,
        "rating": 4.7,
        "enrolled_students": 750,
        "is_active": True,
        "tags": ["django", "web", "python", "backend"],
        "schedule": {"day": "Tuesday", "time": "11:00 AM"}
    },
    {
        "id": "ML301",
        "title": "Machine Learning",
        "instructor": "Dr. Bob Lee",
        "department": "AI & Data Science",
        "duration_weeks": 14,
        "credits": 4,
        "level": "Advanced",
        "price": 349.99,
        "rating": 4.9,
        "enrolled_students": 620,
        "is_active": True,
        "tags": ["ML", "AI", "deep learning", "python"],
        "schedule": {"day": "Thursday", "time": "3:00 PM"}
    },
    {
        "id": "DB201",
        "title": "Database Management",
        "instructor": "Prof. Sara Davis",
        "department": "Computer Science",
        "duration_weeks": 8,
        "credits": 3,
        "level": "Intermediate",
        "price": 199.99,
        "rating": 4.5,
        "enrolled_students": 870,
        "is_active": False,
        "tags": ["SQL", "databases", "PostgreSQL"],
        "schedule": {"day": "Friday", "time": "9:00 AM"}
    },
    {
        "id": "CL401",
        "title": "Cloud Computing with AWS",
        "instructor": "Mr. James Wilson",
        "department": "Cloud & DevOps",
        "duration_weeks": 10,
        "credits": 3,
        "level": "Advanced",
        "price": 299.99,
        "rating": 4.7,
        "enrolled_students": 540,
        "is_active": True,
        "tags": ["AWS", "cloud", "DevOps"],
        "schedule": {"day": "Monday", "time": "1:00 PM"}
    }
]


# ------------------------------------------------------------
# 5. filter() — Filter courses by level
# ------------------------------------------------------------
immediate_level_courses = list(filter(lambda course: course['level'] == 'Intermediate', courses))
immediate_level_courses

beginner_level_courses = list(filter(lambda course: course['level'] == 'Beginner', courses))
beginner_level_courses

advanced_level_courses = list(filter(lambda course: course['level'] == 'Advanced', courses))
advanced_level_courses


# ------------------------------------------------------------
# 6. filter() — Reusable function version
# ------------------------------------------------------------
def filter_courses_by_level(level):
    filtered_courses = list(filter(lambda course: course['level'] == level, courses))
    return filtered_courses

filter_courses_by_level('Intermediate')


# ------------------------------------------------------------
# 7. reduce() — Sum of transactions
# ------------------------------------------------------------
from functools import reduce

transactions = [7000, 5500, 4900, 3400]

total_amount = reduce(lambda accumulator, transaction: accumulator + transaction, transactions)
total_amount
# Output: 20800


# ------------------------------------------------------------
# 8. Sample Dataset — Products
# ------------------------------------------------------------
products = [
    {
        "product_id": "PRD001",
        "name": "MacBook Pro 14",
        "category": "Laptops",
        "brand": "Apple",
        "price": 1999.99,
        "discount": 10,
        "stock": 50,
        "quantity": 2,
        "rating": 4.8,
        "is_available": True
    },
    {
        "product_id": "PRD002",
        "name": "Samsung Galaxy S24",
        "category": "Smartphones",
        "brand": "Samsung",
        "price": 899.99,
        "discount": 15,
        "stock": 120,
        "quantity": 5,
        "rating": 4.6,
        "is_available": True
    },
    {
        "product_id": "PRD003",
        "name": "Sony WH-1000XM5",
        "category": "Headphones",
        "brand": "Sony",
        "price": 349.99,
        "discount": 20,
        "stock": 75,
        "quantity": 3,
        "rating": 4.9,
        "is_available": True
    },
    {
        "product_id": "PRD004",
        "name": "Dell UltraSharp 27",
        "category": "Monitors",
        "brand": "Dell",
        "price": 599.99,
        "discount": 5,
        "stock": 30,
        "quantity": 1,
        "rating": 4.7,
        "is_available": True
    },
    {
        "product_id": "PRD005",
        "name": "iPad Air 5th Gen",
        "category": "Tablets",
        "brand": "Apple",
        "price": 749.99,
        "discount": 8,
        "stock": 0,
        "quantity": 0,
        "rating": 4.7,
        "is_available": False
    },
    {
        "product_id": "PRD006",
        "name": "Logitech MX Master 3",
        "category": "Accessories",
        "brand": "Logitech",
        "price": 99.99,
        "discount": 12,
        "stock": 200,
        "quantity": 10,
        "rating": 4.8,
        "is_available": True
    },
    {
        "product_id": "PRD007",
        "name": "LG OLED 55 inch TV",
        "category": "Televisions",
        "brand": "LG",
        "price": 1299.99,
        "discount": 18,
        "stock": 20,
        "quantity": 1,
        "rating": 4.9,
        "is_available": True
    },
    {
        "product_id": "PRD008",
        "name": "Canon EOS R50",
        "category": "Cameras",
        "brand": "Canon",
        "price": 679.99,
        "discount": 7,
        "stock": 0,
        "quantity": 1,
        "rating": 4.5,
        "is_available": False
    },
    {
        "product_id": "PRD009",
        "name": "Dyson V15 Vacuum",
        "category": "Home Appliances",
        "brand": "Dyson",
        "price": 749.99,
        "discount": 10,
        "stock": 45,
        "quantity": 2,
        "rating": 4.6,
        "is_available": True
    },
    {
        "product_id": "PRD010",
        "name": "Nike Air Max 270",
        "category": "Footwear",
        "brand": "Nike",
        "price": 149.99,
        "discount": 25,
        "stock": 300,
        "quantity": 4,
        "rating": 4.4,
        "is_available": True
    }
]


# ------------------------------------------------------------
# 9. reduce() — Total amount after discount, weighted by quantity
# ------------------------------------------------------------
total_amount = reduce(
    lambda accumulator, product: accumulator + (product['price'] - (product['price'] * product['discount'] / 100) * product['quantity']),
    products,
    0
)
total_amount
# Output: 5503.3432999999995