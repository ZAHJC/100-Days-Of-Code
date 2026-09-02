from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.reset_position()

    def reset_position(self):
        randomX = random.randint(-280,280)
        randomY = random.randint(-280,280)
        self.goto(x=randomX,y=randomY)
