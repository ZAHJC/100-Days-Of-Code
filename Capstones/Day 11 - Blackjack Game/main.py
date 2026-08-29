import art
import random
from pprint import pprint
cardNames = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
score = 0
gameState = "Y"
computerUnder17 = False
playerChecked = 'N'

def create_deck(cards):
    """Create a dictionary with the values of each card"""
    deck = {}
    counter = 0
    for name in cardNames:
        if name == "Ace":
            deck[name] = 1 , 11
        elif name == "Jack" or name == "Queen" or name == "King":
            deck[name] = 10
        else:
            deck[name] = counter+1
        counter += 1
    return deck

def first_deal(deck):
    """Computes the first set of cards for the computer and player returns dictionary"""
    timesToDeal = 2
    dealtHands = {
        "Computer" : {
            "Cards": [],
            "Score" : 0
             },
        "Player" : {
            "Cards": [],
            "Score" : 0
        }
    }
    while timesToDeal > 0:
        cardChosen = random.choice(list(deck))
        dealtHands["Computer"]["Cards"].append(cardChosen)
        cardChosen = random.choice(list(deck))
        dealtHands["Player"]["Cards"].append(cardChosen)
        timesToDeal -= 1
    return dealtHands

def checked(currentHand, cardNames, whoChecked):
    """deals one card to the player or deals with dealing to the computer at end of game"""
    if whoChecked == "Computer":
        currentHand["Computer"]["Cards"].append(random.choice(cardNames))
        return currentHand
    else:
        currentHand["Player"]["Cards"].append(random.choice(cardNames))
        return currentHand

def update_score(currentHand, deck, whoChecked):
    """Updates users score and returns the dict"""
    newScore = 0
    aces = 0

    for card in currentHand[whoChecked]["Cards"]:
        if card == "Ace":
            newScore += 11
            aces += 1
        else:
            newScore += deck[card]

    while newScore > 21 and aces > 0:
        newScore -= 10
        aces -= 1

    currentHand[whoChecked]["Score"] = newScore

    return currentHand

def display_cards_and_score(currentHand):
    """Deals with printing the in play scores and cards of the player and computer, dealing with a blackjack state also"""
    playerString = (
        f"  Your cards are {currentHand['Player']['Cards']} "
        f"Your score is {currentHand['Player']['Score']}"
    )
    playerBlackjackString = (
        f"  Your cards are {currentHand['Player']['Cards']} "
        "YOU HAVE BLACKJACK"
    )
    computerBlackjackString = (
        f"  Computer's cards are {currentHand['Computer']['Cards']} "
        f"DEALER HAS BLACKJACK"
    )
    computerFirstCard = (
        f"  The computers first card is {currentHand['Computer']['Cards'][0]}"
    )

    parsedPlayerString = playerString.replace("'", "")
    parsedComputerString = computerFirstCard.replace("'", "")
    parsedPlayerBlackjackString = playerBlackjackString.replace("'", "")
    parsedComputerBlackjackString = computerBlackjackString.replace("'", "")

    if currentHand["Player"]["Score"] == 21:
        print(parsedPlayerBlackjackString)
        print(parsedComputerString)
        return
    elif currentHand["Computer"]["Score"] == 21:
        print(parsedPlayerString)
        print(parsedComputerBlackjackString)
        return
    else:
        print(parsedPlayerString)
        print(parsedComputerString)
        return

def final_cards(currentHand):
    """Generates the strings to print the final cards of the player and computer and prints them"""
    playerString = (
        f"  Your cards are {currentHand['Player']['Cards']} "
        f"Your score is {currentHand['Player']['Score']}"
    )
    computerFullString = (
        f"  Computer's cards are {currentHand['Computer']['Cards']} "
            f"Computer's score is {currentHand['Computer']['Score']}"
    )
    parsedComputerFullString = computerFullString.replace("'", "")
    parsedPlayerString = playerString.replace("'", "")
    print(parsedPlayerString)
    print(parsedComputerFullString)

# Sets game state, sets up dictionary assigning correct value to card and deals fors hand
print(art.logo)
gameState = input("Would you like to play a game of blackjack? Yes (Y) No (N): ").capitalize()
cardDict = create_deck(cardNames)
dealtHands = first_deal(cardDict)

# Core game loop
while gameState == "Y":
    dealtHands = update_score(dealtHands, cardDict, "Player")
    dealtHands = update_score(dealtHands, cardDict, "Computer")

    if dealtHands["Player"]["Score"] < 21:
        display_cards_and_score(dealtHands)

    if dealtHands["Player"]["Score"] < 21:

        playerChecked = input("Would you like to draw another card (Y) (N): ").capitalize()

        if playerChecked == "Y":
            dealtHands = checked(dealtHands, cardNames, "Player")
            continue
    else:
        # Handles the computer pulling cards once player has and states of winning or losing
        while dealtHands["Computer"]["Score"] < 17:
            dealtHands = checked(dealtHands, cardNames, "Computer")
            dealtHands = update_score(dealtHands, cardDict, "Computer")

        final_cards(dealtHands)

        if dealtHands["Player"]["Score"] > 21:
            print("You LOST — you busted!")
            gameState = input("Would you like to play another game? Yes (Y) No (N): ").capitalize()
            dealtHands = first_deal(cardDict)
            print("\n" * 20)
            print(art.logo)

        elif dealtHands["Computer"]["Score"] > 21:
            print("You WIN — computer busted!")
            gameState = input("Would you like to play another game? Yes (Y) No (N): ").capitalize()
            dealtHands = first_deal(cardDict)
            print("\n" * 20)
            print(art.logo)

        elif dealtHands["Computer"]["Score"] > dealtHands["Player"]["Score"]:
            print("You LOST")
            gameState = input("Would you like to play another game? Yes (Y) No (N): ").capitalize()
            dealtHands = first_deal(cardDict)
            print("\n" * 20)
            print(art.logo)

        elif dealtHands["Player"]["Score"] > dealtHands["Computer"]["Score"]:
            print("You WIN")
            gameState = input("Would you like to play another game? Yes (Y) No (N): ").capitalize()
            dealtHands = first_deal(cardDict)
            print("\n" * 20)
            print(art.logo)

        else:
            print("You DRAW")
            gameState = input("Would you like to play another game? Yes (Y) No (N): ").capitalize()
            dealtHands = first_deal(cardDict)
            print("\n" * 20)
            print(art.logo)
