#Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies. 🐝

# Here's the catch:

#    For multiples of 3, print "Fizz" instead of the number.
#    For multiples of 5, print "Buzz" instead of the number.
#    Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

# Write code below 💖

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
