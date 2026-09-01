import random
import turtle
from turtle import Turtle, Screen

#Variables used for application
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("grey")
colorList = ["red", "green", "yellow", "blue", "magenta", "cyan"]
turtleList = []
startPositionY = -100
startPositionX = -240
winPositionX = 240
leadPosition = startPositionX

leadTurtle = Turtle()
leadTurtle.hideturtle()

# Creates turtles based on number of colours
for i in range(0, len(colorList)):
    turtleList.append(Turtle())
    turtleList[i].color(colorList[i])
    turtleList[i].shape("turtle")

# Sets the start position of each turtle
for i in range(0, len(turtleList)):
    turtleList[i].penup()
    if i == 0:
        turtleList[i].goto(-240, startPositionY)
    else:
        turtleList[i].goto(-240, startPositionY+i*40)

# Prompts user to gamble their childs uni fund
userBet=screen.textinput(title="Make your bet", prompt="Which color do you believe will win?")

# Main logic for turtle movement
while leadPosition < winPositionX:
    for i in range(0, len(turtleList)):
        turtleList[i].forward(random.randint(0,16))
    for q in range(0, len(turtleList)):
        if turtleList[q].xcor() > leadPosition:
            leadPosition = turtleList[q].xcor()
            leadTurtle = turtleList[q]

# Checks if user beat the odds (I am yet to win naturally)
if userBet == leadTurtle.fillcolor():
    print(f"You were correct! the {leadTurtle.fillcolor()} turtle won.")
else:
    print(f"Sorry, the {leadTurtle.fillcolor()} turtle was the winner.")

# Allows for a ragequit if Alt or F4 key is broken
screen.exitonclick()