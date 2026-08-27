import random

# ASCII art for the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lists to refer to for accessing ASCII art and names of game choices.
choicesList = [rock, paper, scissors]
choicesNames = ["Rock", "Paper", "Scissors"]

# Welcoming user with instructions
print("Welcome to the Rock Paper Scissors game!")
print("select either Rock(0) or Paper(1) or Scissors(2)")
userChoice = int(input("Please enter your choice: "))

# Calculates the computers decision in the game by rolling a random int and loads the ASCII art to a variable
computerRoll = random.randint(0, len(choicesList)-1)
computerChoice = choicesList[computerRoll]

# If statements determine the conditions of the game and print from variables, reduced hardcoding as much as possible.
# I'm sure there's a better way to do this, will update when I learn it.
if userChoice == 0 and computerRoll == 0:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("Its a DRAW")
if userChoice == 0 and computerRoll == 1:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You LOST")
if userChoice == 0 and computerRoll == 2:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You WON")
if userChoice == 1 and computerRoll == 0:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You WON")
if userChoice == 1 and computerRoll == 1:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("Its a DRAW")
if userChoice == 1 and computerRoll == 2:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You LOST")
if userChoice == 2 and computerRoll == 0:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You LOST")
if userChoice == 2 and computerRoll == 1:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("You WON")
if userChoice == 2 and computerRoll == 2:
    print(f"You chose {choicesNames[userChoice]}")
    print(choicesList[userChoice])
    print(f"The computer chose {choicesNames[computerRoll]}")
    print(computerChoice)
    print("Its a DRAW")