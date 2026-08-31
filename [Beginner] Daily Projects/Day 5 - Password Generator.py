import random

# Lists of characters used to generate
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcomes user and gathers input data for the amount of letters, symbols and numbers they would like within their password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Variable to place the chosen characters.
generatedList = []

# These if statements parse the user input do determine whether it will generate characters for a given type.
# The for loops iterate over the given lists utilising random.choice() to randomly select and then append the given choice to the list containing the characters for the password.
if nr_letters > 0:
    for amount in range(nr_letters):
        letter = random.choice(letters)
        generatedList.append(letter)

if nr_symbols > 0:
    for amount in range(nr_symbols):
        symbol = random.choice(symbols)
        generatedList.append(symbol)

if nr_numbers > 0:
    for amount in range(nr_numbers):
        number = random.choice(numbers)
        generatedList.append(number)

# This will shuffle the generated list of characters as it would uniformly display letters, symbols, and then numbers otherwise.
random.shuffle(generatedList)

# Prints created password
print("".join(generatedList))