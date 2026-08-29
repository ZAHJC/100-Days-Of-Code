import random
import art

# Variables for game
gameState = 1
easyAttemptAmount = 10
hardAttemptAmount = 5
attemptsRemaining = 0
numberGuessed = 0
randomNumber = random.randint(1, 101)
difficulty = ''

# Welcome to game
print(art.logo)
print("Welcome to Number Guessing Project")
print("You have to guess a number between 1 and 100")

# Game loop
while gameState == 1:
    difficulty = input("Choose a difficulty level, type easy or hard: ")

    if difficulty == "easy":
        attemptsRemaining = easyAttemptAmount
        print(f"EASY MODE: you have {attemptsRemaining} attempts")
    elif difficulty == "hard":
        attemptsRemaining = hardAttemptAmount
        print(f"HARD MODE: you have {attemptsRemaining} attempts")
    else:
        print("Invalid Input")
        break

    while attemptsRemaining > 0:
        # Catches any user input that isn't within the bounds
        try:
            numberGuessed = int(input("Choose a number between 1 and 100: "))

            if not 1<=numberGuessed<=10000:
                continue

        except ValueError:
            print("Invalid Input")
            continue

        # Deals with game logic
        if numberGuessed != randomNumber:
            attemptsRemaining -= 1
            if attemptsRemaining == 0:
                break
            if numberGuessed > randomNumber:
                print(f"Too High\nTry Again.\nYou have {attemptsRemaining} attempts left")
            else:
                print(f"Too Low\nTry Again.\nYou have {attemptsRemaining} attempts left")
        elif numberGuessed == randomNumber:
            print("CONGRATULATIONS YOU GUESSED THE NUMBER!")
            break
    if numberGuessed != randomNumber:
        print("Better Luck Next Time!")
    gameState = 0