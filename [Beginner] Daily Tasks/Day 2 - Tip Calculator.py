# Greets User
print("Welcome to the tip calculator!")

# This section covers the initialisation, and declaration of variables required
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

#calculating the total amount each person pays to make up the tip amount.
amount = round(bill * (tip / 100) / people, 2)

#displays amount to user.
print(f"Each person should pay: ${amount}")