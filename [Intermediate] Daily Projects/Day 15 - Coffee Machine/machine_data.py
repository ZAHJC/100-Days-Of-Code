## Keyword for deactivating machine
DEACT_KEYWORD = "off"

# Keyword for generating a report of the current state of the machine
REPORT_KEYWORD = "report"

# Value for coins inserted
PENNY_VAL = 0.01
NICKLE_VAL = 0.05
DIME_VAL = 0.10
QUARTER_VAL = 0.25

# Prompt displayed at startup
INITIAL_PROMPT = "What would you like? (espresso/latte/cappuccino) "

# Menu of items
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources at max capacity
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

