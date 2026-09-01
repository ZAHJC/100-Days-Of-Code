from turtle import Turtle

class Snake:
    def __init__(self):
        self.start_size = 3
        self.body = []
        self.COLOUR = "white"
        self.WIDTH = 20
        self.shape = "square"
        self.create_snake()

    def create_snake(self):
        for i in range(0,self.start_size):
            self.body.append(Turtle())
            self.body[i].shape(self.shape)
            self.body[i].color(self.COLOUR)
            self.body[i].penup()
            if i != 0:
                self.body[i].goto(x=self.body[i-1].xcor()-self.WIDTH, y=0)

    def move_forward(self):
        for i in range(len(self.body)):
            currentXcor = self.body[i].xcor()
            currentYcor = self.body[i].ycor()
            if i == 0:
                self.body[i].forward(self.WIDTH)
            else:
                self.body[i].goto(previousXcor, previousYcor)

            previousXcor = currentXcor
            previousYcor = currentYcor

