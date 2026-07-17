# ------------------------------------------------------------
# INHERITANCE - BASICS
# ------------------------------------------------------------
# Class A = Parent / Base Class
# Class B = Child / Derived Class
# Child class has all the attributes and methods of the parent
# class, along with its own.

class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()  # Super - keyword used to call immediate parent class constructor
        self.y = 20


b = B()
print(b.x)   # 10 (inherited from class A)
print(b.y)   # 20 (own attribute)


# ------------------------------------------------------------
# INHERITANCE - VEHICLE / BIKE EXAMPLE
# ------------------------------------------------------------

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


class Bike(Vehicle):
    def __init__(self, brand, wheels, color):
        super().__init__(brand, wheels)
        self.color = color

    def show_bike_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels} Color: {self.color}")


bike = Bike("Yamaha", 2, "Red")
bike.show_bike_info()   # Brand: Yamaha, Wheels: 2 Color: Red


# ------------------------------------------------------------
# TYPES OF INHERITANCE
# ------------------------------------------------------------

# Multi-level inheritance
# class A:
#     ...
# class B(A):
#     ...
# class C(B):
#     ...

# Hierarchical inheritance
# class A:
#     ...
# class B(A):
#     ...
# class C(A):
#     ...
# class D(A):
#     ...


# ------------------------------------------------------------
# MULTI-LEVEL INHERITANCE EXAMPLE - VEHICLE SYSTEM
# ------------------------------------------------------------

class VehicleBase:
    def start(self):
        print("Vehicle started")


class Car(VehicleBase):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Battery charging")


tesla = ElectricCar()
tesla.start()    # Vehicle started      (inherited from VehicleBase)
tesla.drive()    # Car is driving       (inherited from Car)
tesla.charge()   # Battery charging     (own method)