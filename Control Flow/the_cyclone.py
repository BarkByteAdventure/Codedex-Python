# Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

# Use a combination of relational and logical operators to create the rules:

#   If they are tall enough and have enough credits, print "Enjoy the ride!"
#   Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
#   Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits.
#   Else, print a message saying they have not met either requirement.

# Write code below 💖

print("Welcome to the Cyclone rollercoaster!")
height = int(input('What is your height (cm)? '))
credit = int(input('How many credits do you have? '))

if height >= 137 and credit >= 10:
  print("Enjoy your ride!")
elif height < 137 and credit >=10:
  print("You are not tall enough to ride.")
elif height >= 137 and credit < 10:
  print("You don't have enough credits.")
else:
  print("Sorry but you are not tall enough and also don't have enough credits to ride.")