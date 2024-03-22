#If you slept through your geometry class, a Pythagorean theorem is the relationship 
# between the three sides of a right triangle. It was named after the Greek philosopher
# Pythagoras, born around 570 BC.

# Pythagorean equation looks like: c= (a ** 2 + b ** 2) ** 0.5
# root is written **0.5

#    The a is the length of a short side.
#    The b is the length of another short side.
#   The c is the length of the hypotenuse.

# The hypotenuse is the longest side of the right triangle.
# Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

# Bonus: If you are looking for a harder challenge, try the Quadratic formula!

# Version 1 hypotenuse
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = (a ** 2 + b ** 2) ** 0.5
print(c)


# Version 2 hypotenuse
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = math.sqrt(a**2 + b**2)
print(c)

# Version 1 Quadratic formula
# ax**2 + bx + c = 0
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
d2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(d1)
print(d2)

# Version 2 Quadratic formula
# ax**2 + bx + c = 0
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
d2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(d1)
print(d2)

