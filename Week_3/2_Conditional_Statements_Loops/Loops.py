# 1. List of Dictionaries
employees = [
    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "IT",
        "designation": "Software Engineer",
        "salary": 75000,
        "experience": 3,
        "location": "Hyderabad"
    },
    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "HR",
        "designation": "HR Manager",
        "salary": 68000,
        "experience": 5,
        "location": "Bangalore"
    },
    {
        "employee_id": 103,
        "name": "Arjun Patel",
        "department": "Finance",
        "designation": "Accountant",
        "salary": 55000,
        "experience": 4,
        "location": "Mumbai"
    },
    {
        "employee_id": 104,
        "name": "Sneha Verma",
        "department": "Sales",
        "designation": "Sales Executive",
        "salary": 50000,
        "experience": 2,
        "location": "Chennai"
    },
    {
        "employee_id": 105,
        "name": "Kiran Kumar",
        "department": "IT",
        "designation": "DevOps Engineer",
        "salary": 82000,
        "experience": 6,
        "location": "Pune"
    },
    {
        "employee_id": 106,
        "name": "Meera Joshi",
        "department": "Marketing",
        "designation": "Marketing Analyst",
        "salary": 60000,
        "experience": 3,
        "location": "Delhi"
    },
    {
        "employee_id": 107,
        "name": "Vikram Singh",
        "department": "Operations",
        "designation": "Operations Manager",
        "salary": 90000,
        "experience": 8,
        "location": "Noida"
    },
    {
        "employee_id": 108,
        "name": "Anjali Nair",
        "department": "Support",
        "designation": "Technical Support Engineer",
        "salary": 48000,
        "experience": 2,
        "location": "Kochi"
    }
]

# You can access values like this:
print(employees[1]["name"])

for employee in employees:
    print(employee)

# Print Employee Number
i=1

for employee in employees:
    print("Employee ", i)
    print(employee)
    i += 1
# Print Employee Details
i=1

for employee in employees:
    print("Employee:", i)
    print(f'Employee ID: {employee["employee_id"]}')
    print(f'Name: {employee["name"]}')
    print(f'Department: {employee["department"]}')
    print(f'Designation: {employee["designation"]}')
    print(f'Salary: {employee["salary"]}')
    print(f'Experience: {employee["experience"]}')
    print(f'Location: {employee["location"]}')

    i += 1

# Print Separator Line
i=1

for employee in employees:
    print("-" * 20)
    print(f'Employee:', i)
    print(f'Employee ID: {employee["employee_id"]}')
    print(f'Name: {employee["name"]}')
    print(f'Department: {employee["department"]}')
    print(f'Designation: {employee["designation"]}')
    print(f'Salary: {employee["salary"]}')
    print(f'Experience: {employee["experience"]}')
    print(f'Location: {employee["location"]}')

    i += 1

# Loop Through Tuple (Months)
months = ("January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December")

for month in months:
    print(month)

# Loop Through String
company_name = "Data Valley"

for char in company_name:
    print(char)

# Dictionary items()
employee_info = {
    "employee_id":101,
    "name":"Rahul Sharma",
    "department":"IT",
    "designation":"Software Engineer",
    "salary":75000,
    "experience":3,
    "location":"Hyderabad"
}

print(employee_info.items()) #.items() returns all key-value pairs.

# Loop Through Dictionary
for key, value in employee_info.items():
    print(key, value)

# Another Way
for employee in employee_info.items():
    print(employee)
    print(employee[0], employee[1])

# range()
for i in range(0,5):
    print("In for Loop")

# range() with List
colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Orange"
]

for i in range(0, len(colors)):
    print(colors[i])

# ##while Loop##
counter = 0

while counter<5:
    print("Counter:", counter)
    counter += 1

# Employee Login Attempts

employee_info = {
    "employee_id": 101,
    "name": "Rahul Sharma",
    "pin": "3450",
    "department": "IT",
    "designation": "Software Engineer",
    "salary": 75000,
    "experience": 3,
    "location": "Hyderabad"
}

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_employee_id = int(input("Enter employee id: "))
    entered_pin = input("Enter pin: ")

    if entered_employee_id == employee_info["employee_id"] and entered_pin == employee_info["pin"]:
        print("Credentials are correct")
        break
    else:
        attempts += 1
        print(f'Invalid credentials, {max_attempts - attempts} attempts left')








