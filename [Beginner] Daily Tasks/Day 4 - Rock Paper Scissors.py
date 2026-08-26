import random

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

choicesList = [rock, paper, scissors]
choicesNames = ["Rock", "Paper", "Scissors"]

print("Welcome to the Rock Paper Scissors game!")
print("select either Rock(0) or Paper(1) or Scissors(2)")


userChoice = int(input("Please enter your choice: "))
computerRoll = random.randint(0, len(choicesList)-1)
computerChoice = choicesList[computerRoll]


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