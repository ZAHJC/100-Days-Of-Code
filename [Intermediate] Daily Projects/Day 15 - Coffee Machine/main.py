import machine_data
currentResources = machine_data.resources
machineState = 1
userChoice = {}


def process_coins(item_chosen):
    """Process coins entered returning the value overall that has been put in"""
    total_entered = int(input("How many pennies entered: ")) * machine_data.PENNY_VAL
    total_entered += int(input("How many nickles entered: ")) * machine_data.NICKLE_VAL
    total_entered += int(input("How many dimes entered: ")) * machine_data.DIME_VAL
    total_entered += int(input("How many quarters entered: ")) * machine_data.QUARTER_VAL

    return total_entered

def check_resources(item_chosen, currentResources):
    """Process if there is enough resources available for this item"""
    for ingredient in item_chosen["ingredients"]:
        if currentResources[ingredient] <= item_chosen["ingredients"][ingredient]:
            return False

    return True

# Overall application logic
while machineState == 1:

    # Prints initial prompt awaiting user inpur
    userInput = input(machine_data.INITIAL_PROMPT)

    # Checks for deactivation keyword
    if userInput == machine_data.DEACT_KEYWORD:
        machineState = 0
        continue
    # Check for the report keyword
    elif userInput == machine_data.REPORT_KEYWORD:
        for resource in currentResources:
            print(f"{resource}: {currentResources[resource]}")
        continue
    elif userInput in machine_data.MENU:
        for item in machine_data.MENU:
            if userInput == item:
                userChoice = machine_data.MENU[item]

        # Assigns overall sum of coins entered
        totalEntered = process_coins(userChoice)

        # Checks if change is required
        if totalEntered > userChoice["cost"]:
            change = totalEntered - userChoice["cost"]
        else:
            change = 0

        # Deals with logic for pouring coffee and dispensing change or notifying if incapable of
        if totalEntered >= userChoice["cost"]:
           resourceCheck = check_resources(userChoice, currentResources)
           if resourceCheck:
               for ingredient in userChoice["ingredients"]:
                   currentResources[ingredient] -= userChoice["ingredients"][ingredient]
               if change > 0:
                   print(f"You have been given ${float('%2f' % change)} in change.")
           elif not resourceCheck:
               print(f"Sorry, the machine does not have the resources for this item. You have been refunded ${float('%2f' % totalEntered)}.")
        else:
            print("Sorry, you dont have enough money for that item.")
    # Deals with any input other than what is possible
    else:
        print("Sorry, that input is invalid, please try again.")
        continue