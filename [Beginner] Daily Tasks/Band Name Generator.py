# Organising and declaring variables to be used
cityName = ""
petName = ""
bandName = ""
greeting = "This little quirky funny thing will generate a band name for you based off of some details about you!\n"

# Greets user and informs on application use
print(greeting)

# Takes user input
petName = input("Lets begin with your pets name?\n")
cityName = input("Great, now what is the name of your city?\n")

# Concatenates strings to form a band name
bandName = (cityName + " " + petName)

# Prints band name
print("NOW LETS HEAR IT FOR!\n" + bandName)