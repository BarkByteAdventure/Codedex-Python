# We just got home from a trip to South America, specifically Colombia, Peru, and Brazil.
# There's some leftover cash in:

#    Colombian pesos
#    Peruvian soles
#    Brazilian reais

# Create a currency.py program that asks the user for the amount they have in pesos, soles,
# and reais and calculates the total in USD.

# Make sure to Google the current exchange rates!

print("Welcome to the currency calculator!")

pesos = float(input("What do you have left in pesos? "))
soles = float(input("What do you have left in soles? "))
reais = float(input("What do you have left in reais) "))

print(f"Lets summarize to be sure. You have {pesos} pesos, {soles} soles, and {reais} reais.")

peso_exchange = pesos * 0.06
print(f"Your pesoso in dollars is the amount of{peso_exchange}$.")
soles_exchange = soles * 0.27
print(f"Your soles in dollars is the amount of {soles_exchange}$.")
reais_exchange = reais * 0.2
print(f"Your reais in dollars is  the amount of{reais_exchange}$.")

total_dollar = peso_exchange + soles_exchange + reais_exchange

print(f"You have {total_dollar} dollars in total.")