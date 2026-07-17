# ------------------------------------------------------------
# CAR CLASS
# ------------------------------------------------------------

class Car:

    # Constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method - Writing function inside the class is called as method.
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


car1 = Car("Toyota", "Corolla", 2020)
print(car1.year)          # 2020
print(car1.model)         # 'Corolla'

car2 = Car('Toyota', 'Innova Crysta', 2025)
print(car2.model)         # 'Innova Crysta'

car3 = Car('Toyota', 'Camry', 2022)
print(car3.model)         # 'Camry'

car3.model = 'Fortuner'
print(car3.model)         # 'Fortuner'

car3.year = 2026
print(car3.model)         # 'Fortuner'
print(car3.year)          # 2026

car1.display_info()       # Make: Toyota, Model: Corolla, Year: 2020


# ------------------------------------------------------------
# BANK ACCOUNT CLASS
# ------------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_no = account_number
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposit successful, current balance is {self.account_balance}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrawal successful, current balance is {self.account_balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        print(f"Current balance is {self.account_balance}")

    def get_account_details(self):
        print(f"Account Number: {self.account_no}, Balance: {self.account_balance}")


account1 = BankAccount(3490, 5000)
print(account1.account_no)         # 3490
print(account1.account_balance)    # 5000

account1.deposit(3450)              # Deposit successful, current balance is 8450
account1.deposit(390)               # Deposit successful, current balance is 8840
account1.withdraw(4500)             # Withdrawal successful, current balance is 4340
account1.get_balance()              # Current balance is 4340
account1.get_account_details()      # Account Number: 3490, Balance: 4340

account2 = BankAccount(5690, 200)
account2.get_balance()              # Current balance is 200
account2.get_account_details()      # Account Number: 5690, Balance: 200


# ------------------------------------------------------------
# EMPLOYEE CLASS (private attributes / encapsulation)
# ------------------------------------------------------------

class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name  # private variable / attribute - can be accessed only within the class.
        self.emp_id = emp_id
        self.salary = salary

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        self.__name = name


emp1 = Employee('Yashwanth', 902, 60000)
print(emp1.salary)          # 60000

# emp1.name would raise:
# AttributeError: 'Employee' object has no attribute 'name'
# because __name is private and name-mangled to _Employee__name

print(emp1.get_name())      # 'Yashwanth'

emp1.set_name('Varun')
print(emp1.get_name())      # 'Varun'