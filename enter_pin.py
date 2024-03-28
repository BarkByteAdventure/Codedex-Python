# Before we dive deep into while loop, let's see a demo using a bank's ATM. 🏦

# Create an enter_pin.py program and type in the following:

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

# Next, press the "Run" button to see the messages print to the terminal.

# Try the following in the terminal on the right 👉:

#   1) Type 1111 and then the enter key.
#   2) Type 2023 and then the enter key.
#   3) Type 1991 and then the enter key.
#   4) Type 1234 and then the enter key.
