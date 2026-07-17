class A:
    def __init__(self):
        self.x = 10
    
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20

b = B()
print(b.x)
print(b.y)

# ------------------------------------------------------------
# INHERITANCE - VEHICLE / BIKE EXAMPLE
# ------------------------------------------------------------

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_info(sel):
        print(f'Brand: {brand}, Wheels: {wheels}')

class Bike(Vehicle):
    def __init__(self, brand, wheels, color):
        # self.brand = brand
        # self.wheels = wheels
        super().__init__(brand, wheels)
        self.color = color

    def show_bike_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels} Color: {self.color}")

bike = Bike("Yamaha", 2, "Red")
bike.show_bike_info()

