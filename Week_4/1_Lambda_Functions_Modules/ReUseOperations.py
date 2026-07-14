from MathOperations import add, subtract, multiply, divide, floor_divide, modulus, power
print(add(4,5))

print(subtract(5,10))
print(multiply(5,10))
print(divide(5,10))
print(floor_divide(5,10))
print(modulus(5,10))
print(power(5,10))

import testp.MathOperations as mo
print(mo.add(10,20))

from testp.MathOperations import add
print(add(15,20))
