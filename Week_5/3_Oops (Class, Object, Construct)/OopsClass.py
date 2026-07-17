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
print(car1.make)
print(car1.model)
print(car1.year)

car2 = Car('Toyota', 'Innova Crysta', 2025)
print(car2.make)
print(car2.model)
print(car2.year)

car3 = Car('Toyota', 'Camry', 2022)
print(car3.model)

car3.model = 'Fortuner'
print(car3.model)

car3.year = 2026
print(car3.year)
print(car3.model)

car1.display_info()
car2.display_info()
car3.display_info()

# ------------------------------------------------------------
# BANK ACCOUNT CLASS
# ------------------------------------------------------------
class BankAccount:
    def __init__(self, account_number, balance = 0):
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
print(account1.account_no)
print(account1.account_balance)

account1.deposit(3450)
account1.deposit(390)
account1.withdraw(4500)
account1.get_balance()

account2 = BankAccount(5690, 200)
account2.get_balance()
account2.get_account_details()