from turtle import Turtle
EAST_BEARING = 0
NORTH_BEARING = 90
WEST_BEARING = 180
SOUTH_BEARING = 270

class Snake:
    def __init__(self):

        self.start_size = 3
        self.body = []
        self.COLOUR = "white"
        self.WIDTH = 20
        self.shape = "square"
        self.create_snake()
        self.head = self.body[0]

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

    def move_left(self):
        if self.head.heading() != EAST_BEARING:
            self.head.setheading(WEST_BEARING)
            self.move_forward()
    def move_right(self):
        if self.head.heading() != WEST_BEARING:
            self.head.setheading(EAST_BEARING)
            self.move_forward()
    def move_up(self):
        if self.head.heading() != SOUTH_BEARING:
            self.head.setheading(NORTH_BEARING)
            self.move_forward()
    def move_down(self):
        if self.head.heading() != NORTH_BEARING:
            self.head.setheading(SOUTH_BEARING)
            self.move_forward()