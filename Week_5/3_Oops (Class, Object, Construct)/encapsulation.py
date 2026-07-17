class Employee:
    def __init__(self, name, emp_id, salary):
        self.__name = name   # private variable / attribute - can be accessed only within the class.
        self.emp_id = emp_id
        self.salary = salary

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        self.__name = name

emp1 = Employee('Rakesh', 902, 60000)
print(emp1.salary)
# print(emp1.name)

# emp1.name would raise:
# AttributeError: 'Employee' object has no attribute 'name'
# because __name is private and name-mangled to _Employee__name

print(emp1.get_name())
emp1.set_name("Ramesh")
print(emp1.get_name())