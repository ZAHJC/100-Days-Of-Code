import art

calculatorState = 1

# Setting up calculator functions
def add(n1, n2):
    """Multiplies two numbers"""""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2

#Assigning
calculatorSetup = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

print(art.logo)

# Calculator state check, this then grabs user input and based upon that selects from the dict the correct function call for the operation
while calculatorState == 1:
    number1 = int(input("Enter first number: "))
    chosenOperation = input("Enter operation (+, -, *, /): ")
    number2 = int(input("Enter second number: "))
    print(calculatorSetup[chosenOperation](number1, number2))
    calculatorState = int(input("Do you want to calculate another number? Yes(1), No(0): "))





