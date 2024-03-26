# The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for
# fortune-telling and advice seeking. 🎱

# It's an oversized 8 ball with some of the following answers:

#    Yes - definitely.
#    It is decidedly so.
#    Without a doubt.
#    Reply hazy, try again.
#    Ask again later.
#    Better not tell you now.
#    My sources say no.
#    Outlook not so good.
#    Very doubtful.

# Create a magic8.py program that can respond to any Yes or No questions with a different answer
# each time it executes.

import random

question = input("What do you want to know?\n")

number = random.randint(1, 9)

if number == 1:
    response = "Yes - definitely."
elif number == 2:
    response = "It is decidedly so."
elif number == 3:
    response = "Without a doubt."
elif number == 4:
    response = "Reply hazy, try again."
elif number == 5:
    response = "Ask again later."
elif number == 6:
    response = "Better not tell you now."
elif number == 7:
    response = "My sources say no."
elif number == 8:
    response = "Outlook not so good."
elif number == 9:
    response = "Very doubtful."
else:
    response = "Wrong input"
    
print("Magic 8 Ball says: " + response)