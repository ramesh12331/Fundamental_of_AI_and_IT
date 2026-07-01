# Task: Student Result Management
# Requirement: Create functions to:
    # 1.Calculate total marks
    # 2.Calculate average
    # 3.Assign grade
    # 4.Determine pass/fail

# Input Marks (5 Subjects)
# maths = 85
# science = 78
# english = 92
# social = 74
# computer = 88

def calculate_total(maths, science, english, social, computer):
    return maths + science + english + social + computer

def calculate_average(total):
    return total/5

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def determine_result(avg):
    return "Pass" if avg >= 35 else "Fail"

# Input
maths = 85
science = 78
english = 92
social = 74
computer = 88

# Function Calls
total = calculate_total(maths, science, english, social, computer)
average = calculate_average(total)
grade = assign_grade(average)
result = determine_result(average)

print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)