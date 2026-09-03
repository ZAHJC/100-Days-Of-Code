import random
from turtle import Turtle
import random
import userint

# Bearings
LEFT_DOWN = 225
LEFT_UP = 135
RIGHT_DOWN = 315
RIGHT_UP = 45
LEFT = 180
RIGHT = 0


BALL_SPEED = 5

# List of bearings
START_HEADINGS =[LEFT, RIGHT, RIGHT_DOWN, RIGHT_UP, LEFT_DOWN, LEFT_UP]

# Screen var
SCREEN_HEIGHT = userint.SCREEN_HEIGHT

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setheading(random.choice(START_HEADINGS))

    def reset(self):
        self.goto(0, 0)
        self.setheading(random.choice(START_HEADINGS))

    def move(self):
        if self.ycor() < SCREEN_HEIGHT/2-10 and self.ycor() > -SCREEN_HEIGHT/2+10:
            self.forward(BALL_SPEED)
        elif self.ycor() >= SCREEN_HEIGHT/2-10:
            if self.heading() == LEFT_UP:
                self.setheading(LEFT_DOWN)
                self.forward(BALL_SPEED)
            elif self.heading() == RIGHT_UP:
                self.setheading(RIGHT_DOWN)
                self.forward(BALL_SPEED)
        elif self.ycor() <= -SCREEN_HEIGHT/2+10:
            if self.heading() == LEFT_DOWN:
                self.setheading(LEFT_UP)
                self.forward(BALL_SPEED)
            elif self.heading() == RIGHT_DOWN:
                self.setheading(RIGHT_UP)
                self.forward(BALL_SPEED)

    def ball_rebound(self, player):
        if player == 1:
            if self.heading() == LEFT_DOWN:
                self.setheading(RIGHT_DOWN)
            if self.heading() == LEFT_UP:
                self.setheading(RIGHT_UP)
            if self.heading() == LEFT:
                self.setheading(random.choice([RIGHT_DOWN, RIGHT_DOWN]))
        if player == 2:
            if self.heading() == RIGHT_DOWN:
                self.setheading(LEFT_DOWN)
            if self.heading() == RIGHT_UP:
                self.setheading(LEFT_UP)
            if self.heading() == RIGHT:
                self.setheading(random.choice([LEFT_DOWN, LEFT_UP]))