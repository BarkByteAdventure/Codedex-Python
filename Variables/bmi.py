# The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used
# by health and nutrition professionals to estimate human body fat in certain populations.

# It is computed by taking an individual's weight (mass) in kilograms and dividing it by the
# square of their height in meters.

# bmi= mass / (height*height)

weight = float(input("Enter your weight in kg: "))
height= float(input("Enter your height in meters: "))

bmi = weight / ( height ** 2)

print(bmi)