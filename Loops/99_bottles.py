#"99 Bottles of Beer" is an old song that annoying kids, oops I mean everyone, sang on road trips to pass the time.

# Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."

# Write code below 💖

# String concatenation

for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print("Take one down, pass it around")
    if bottles == 1:
        print("No more bottles of beer on the wall")
    else:
        print(f"{bottles - 1} bottle{'s' if bottles - 1 != 1 else ''} of beer on the wall")
    print()