from turtle import Turtle
import userint

# Easier adjustment of paddle vars
PADDLE_SPEED = 25
PADDLE_WIDTH = 5
SCREENWIDTH = userint.SCREEN_WIDTH

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.playerID = 0
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_WIDTH)
        self.color("white")

    def set_location(self):
        if self.playerID== 1:
            self.goto(x=-SCREENWIDTH/2+20,y=0)
        elif self.playerID == 2:
            self.goto(x=SCREENWIDTH/2-30,y=0)

    def move_up(self):
        self.forward(PADDLE_SPEED)
    def move_down(self):
        self.backward(PADDLE_SPEED)

    def check_overlap(self, item):
        x_overlap = abs(self.xcor() - item.xcor()) <= 10
        y_overlap = abs(self.ycor() - item.ycor()) <= 50

        return x_overlap and y_overlap