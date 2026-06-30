# Practice Task 1 – Student Grade Calculator
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Practice Task 2 – Online Shopping Discount
amount = float(input("Enter Cart Amount: "))
premium = input("Premium User (yes/no): ").lower()

discount = 0

if amount > 10000:
    discount = 20
elif amount > 5000:
    discount = 10
elif amount > 2000:
    discount = 5

if premium == "yes":
    discount += 5

print(f'Total Discount: {discount}%')
