# Imports artwork
import art

bidDict = {} # For storing all names and bids
auctionState = 1 # Used to check auction state
highestBidder = ["", 0] # Stores highest bidder

print(art.logo)

print("Welcome to the blind auction program!\n")

while auctionState == 1:
    name = input("Enter your name: ")
    bidDict[name] = input("Enter your bid: $") # Stores bid in dict
    auctionState = int(input("Do you have more entries? Yes(1), No(0)")) # Checks state
    print("\n"*20) # Clears screen

# Compares bids and stors highest bid data in the highestBidder list
for name in bidDict:
    if int(bidDict[name]) > int(highestBidder[1]):
        highestBidder[0] = name
        highestBidder[1] = bidDict[name]

# Prints winner
print(f"The highest bid is {highestBidder[0]}. With a bid of ${highestBidder[1]}.")