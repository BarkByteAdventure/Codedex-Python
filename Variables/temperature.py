# Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).
# Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

# Use the following formula and write it out in Python:

# Celsius= (Fahrenheit−32)​ / 1.8

#Print out the converted temperature.

temp_fahrenheit = 43

temp_celsius = (temp_fahrenheit - 32) / 1.8

new_celsius= round(temp_celsius, 2)

print(new_celsius)