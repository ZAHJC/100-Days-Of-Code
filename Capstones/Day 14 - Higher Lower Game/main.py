import random
import game_data
import art

gameState = 1
score = 0

# Sets a random item to each options for initialisation
firstChoice = random.choice(game_data.data)
secondChoice = random.choice(game_data.data)

while gameState == 1:
    print(art.logo)

    # Checks score, prints if it has been set
    if score > 0:
        print(f"THATS RIGHT! Score: {score}")


    # Checks that choices are not the same as each other
    if firstChoice == secondChoice:
        while firstChoice == secondChoice:
            secondChoice = random.choice(game_data.data)

    # Prints information to screen
    print(f"Compare A: {firstChoice['name']}, {firstChoice['description']}, from {firstChoice['country']}")
    print(art.vs)
    print(f"Compare B: {secondChoice['name']}, from {secondChoice['country']}, from {secondChoice['country']}")
    choice = input("Who has more followers (A/B): ").capitalize()

    # Checks user choice and runs game logic for said choice, including failure state
    if choice == "A":
        if firstChoice["follower_count"] > secondChoice["follower_count"]:
            score += 1
            firstChoice = secondChoice
            secondChoice = random.choice(game_data.data)
        else:
            print("\n"*20)
            print(f"Sorry, that's wrong. Final Score: {score}")
            gameState = 0
    elif choice == "B":
        if secondChoice["follower_count"] > firstChoice["follower_count"]:
            score += 1
            firstChoice = secondChoice
            secondChoice = random.choice(game_data.data)
        else:
            print("\n" * 20)
            print(f"Sorry, that's wrong. Final Score: {score}")
            gameState = 0
