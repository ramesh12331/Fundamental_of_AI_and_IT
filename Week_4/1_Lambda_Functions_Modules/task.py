employees = [
    {"name": "John", "salary": 70000},
    {"name": "Alice", "salary": 90000},
    {"name": "Bob", "salary": 80000}
]

def sort_by_salary(emp_list):
    return sorted(emp_list, key=lambda emp: emp["salary"])

print(sort_by_salary(employees))