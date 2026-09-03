from turtle import Turtle
import scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=random.randrange(300, 500), y=random.randrange(-230, 260))
        self.setheading(180)
        self.shapesize(stretch_wid=0.95, stretch_len=1.90)
        self.movespeed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.movespeed)

    def reset(self):
        self.goto(x=random.randrange(300, 400), y=random.randrange(-250, 250))

    def check_collision(self, player):
        xcollision = abs(self.xcor() - player.xcor()) < 25
        ycollision = abs(self.ycor() - player.ycor()) < 20
        return xcollision and ycollision

    def increase_speed(self):
        self.movespeed += MOVE_INCREMENT