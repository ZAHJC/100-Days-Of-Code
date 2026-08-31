from turtle import Turtle, Screen
import colorgram
import random

# Variable declaration and initialization
myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)
myScreen.setup(500, 400)
width = myScreen.window_width()
height = myScreen.window_height()
myTurtle.pensize(20)
dotCanvas = 100
rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# sets row start point
xPoint = -250

# Sends turtle to start point
myTurtle.penup()
myTurtle.goto(xPoint, -300)


for x in range(0, int(dotCanvas/10)):
    for i in range(0, 10):
        myTurtle.dot(20, random.choice(rgb_colors))
        myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(50)
    currentYPosition = myTurtle.position()[1]
    myTurtle.setposition(xPoint, currentYPosition)
    myTurtle.right(90)


myScreen.exitonclick()
