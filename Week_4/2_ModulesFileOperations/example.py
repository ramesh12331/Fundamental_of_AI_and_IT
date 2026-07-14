import datetime
current_time = datetime.datetime.now()
print(current_time.strftime('%H:%M:%S'))
# Output: 15:32:48

print(current_time.strftime('%d-%m-%Y'))
# Output: 14-07-2026

print(current_time.strftime('%A, %B %d, %Y'))
# Output: Tuesday, July 14, 2026

print(current_time.strftime('%I:%M:%S %p:%Z %z'))
# Output: 03:32:48 PM:  (blank %Z and %z since this datetime has no tzinfo)

from datetime import datetime, timezone

# Without timezone info (blank %Z and %z)
current_time = datetime.now()
print(current_time.strftime('%I:%M:%S %p:%Z %z'))
# Output: 03:32:48 PM:  (blank timezone)

# With UTC timezone
current_time_utc = datetime.now(timezone.utc)
print(current_time_utc.strftime('%I:%M:%S %p:%Z %z'))
# Output: 03:32:48 PM:UTC +0000

india_file = open('india.txt', 'r')
content = india_file.readlines()
print(content)
# Output: ["India, officially the Republic of India,[j][19] is a country in South Asia. It is the seventh-largest country by area; the most populous country in the world[20] and, since its independence in 1947, the world's most populous democracy.[21][22][23] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[k] China, Nepal and Bhutan to the north; Bangladesh and Myanmar to the east. In the Indian Ocean, India is near Sri Lanka and the Maldives. Its Andaman and Nicobar Islands share a maritime border with Myanmar, Thailand and Indonesia."]

# india_file.close()

# with open('india.txt', 'r') as india_file:
#     content = india_file.readlines()
#     print(content)

# india_file = open('india.txt', 'w')
# india_file.write('India is a great country. \n')
# india_file.write('Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.')
# india_file.close()

india_file = open('india.txt', 'a')
india_file.write('\n India is a great country. \n')
india_file.write('Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.')
india_file.writelines(['\n India is a great country. \n', 'Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.'])
india_file.close()
# No print here -- these lines append text to india.txt on disk (no console output)

with open('Flag_of_India.webp', 'rb') as flag_file:
    content = flag_file.read()
    print(content)
    # Output: b'RIFF\x14\n\x00\x00WEBPVP8\x08...' (raw binary bytes of the image file)

import csv

with open('students.csv', 'r') as students_file:
    # csv_reader = csv.reader(students_file)
    # for row in csv_reader:
    #     print(row)

    csv_reader = csv.DictReader(students_file)
    for row in csv_reader:
        print(row)
        # Output (one dict per row), e.g.:
        # {'student_id': 'STU001', 'name': 'Alice Johnson', 'age': '20', 'gender': 'Female', 'email': 'alice.johnson@university.edu', 'phone': '+1-555-0101', 'department': 'Computer Science', 'year': '2', 'gpa': '3.8', 'attendance': '92', 'grade': 'A', 'city': 'New York', 'country': 'USA', 'scholarship': 'True', 'is_active': 'True'}
        # {'student_id': 'STU002', 'name': 'Bob Smith', 'age': '21', 'gender': 'Male', ...}
        # {'student_id': 'STU003', 'name': 'Carol White', 'age': '19', 'gender': 'Female', ...}
        # ... one dict per remaining row in students.csv

students_lol = [
    ["STU001", "Alice Johnson", 20, "Computer Science", 3.8, "A"],
    ["STU002", "Bob Smith", 21, "Mathematics", 3.2, "B"],
    ["STU003", "Carol White", 19, "Physics", 3.9, "A"],
    ["STU004", "David Brown", 22, "Engineering", 2.8, "C"],
    ["STU005", "Eva Martinez", 20, "Data Science", 3.6, "A"],
    ["STU006", "Frank Lee", 23, "Computer Science", 3.1, "B"],
    ["STU007", "Grace Kim", 21, "AI & ML", 3.9, "A"],
    ["STU008", "Henry Wilson", 22, "Business", 2.5, "C"],
    ["STU009", "Isla Thompson", 19, "Psychology", 3.4, "B"],
    ["STU010", "James Davis", 20, "Computer Science", 3.7, "A"],
]

with open('students.csv', 'a', newline='') as students_file:
    csv_writer = csv.writer(students_file)
    result = csv_writer.writerows(students_lol)
    print(result)
    # No print here -- this appends the 10 rows in students_lol to students.csv on disk (no console output)
    