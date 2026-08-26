#Sets the Gamestate
gameState = 1

# Intro visual
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# This section displays the background and the rules of the game.
print("Welcome to The Adventure of the Crystal Kingdom")
print("You are partaking on a mystical journey through the lands of Ayr to collect the kingdom crystals so that you may save them from being stolen by the Illiads")
print("when you see (...) , press enter to continue the text || when a number is in brackets like this (1) that is the number to enter to choose that decision.")


# Play state of game, takes user input as integers and evaluates the input using if and elif and checks the gamestate to make sure player is still alive to avoid any mishaps

print("\nyou have come upon a split in the pathway through the castle, which way do you go, left(1) or right(2)?")
userInput = int(input())
if userInput == 1 and gameState == 1:
    print("Great, you managed to make it to the crystalis, the storage room for the kindom crystals...")
    input()
    print("You hear a knock on the door! do you hide and wait(1) or do you dive out the window into the winding river(2)?")
    userInput = int(input())
elif userInput != 1 and gameState == 1:
    print("You have come across Bumblemore the wizard...")
    input()
    print("He casts polymorph and turns you into a frog")
    print("YOU DIED")
    gameState = 0

if userInput == 1 and gameState == 1:
    print("Bumblemore the wizard opens the door and checks the room but did not spot you and returns to his chambers, lucky you.\nyou decide to take a different route out of the castle and come to three doors a Red(1) door, a blue door(2), a green door(3).")
    userInput = int(input())
elif userInput != 1 and gameState == 1:
    print("You dive out the window head first into the winding river...")
    input()
    print("You are just about to make it to shore when you are pulled back by the tentacle of the Squidclopse! A rare sighting, such opportune circumstances.")
    print("YOU DIED")
    gameState = 0

if userInput == 1:
    # did this myself to add a little flair to the game, iterates over itself as it's a door that leads to the same room
    while userInput == 1 and gameState == 1:
        print("You have chosen the red door, somehow you have arrived at the same room, do you pick the Red(1) door, blue door(2), green door(3)")
        userInput = int(input())
        if userInput != 1:
            break
if userInput == 2 and gameState == 1:
    print("you open it up and look inside...")
    input()
    print("little did you know this was the master door to the magical dungeon, out pours demons of all kind that stampede out and trample you to death.")
    print("YOU DIED")
    gameState = 0
elif userInput == 3 and gameState == 1:
    print("You picked the green door, \"Green means go right?\"...")
    input()
    print("CORRECT")
    print("you have escaped the castle with the kingdom crystals, congratulations you have saved the kingdom and may return to your home.1")
    gameState = 0