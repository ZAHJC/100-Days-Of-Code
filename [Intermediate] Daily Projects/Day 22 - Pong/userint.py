from turtle import Turtle, Screen
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCOREBOARD_POSITION = [225, 250]
FONT_SIZE = 30
FONT = "Ithaca"

class UserInterface():
    def __init__(self):
        self.screen = Screen()
        self.centreline = Turtle()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.setup_centreline()

    def setup_centreline(self):
        self.centreline.hideturtle()
        self.centreline.penup()
        self.centreline.pencolor("white")
        self.centreline.goto(x=SCREEN_WIDTH*0, y=SCREEN_HEIGHT/2)
        self.centreline.setheading(270)
        for i in range(0, int(SCREEN_HEIGHT/20)):
            if i % 2 == 0:
                self.centreline.penup()
                self.centreline.forward(20)
            elif i % 2 != 0:
                self.centreline.pendown()
                self.centreline.forward(20)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.p1score = 0
        self.p2score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_score()


    def write_score(self):
        self.clear()
        self.goto(x=-SCOREBOARD_POSITION[0], y=SCOREBOARD_POSITION[1])
        self.write(f"{self.p1score}", align="center", font=(FONT, FONT_SIZE, "normal"))
        self.goto(x=SCOREBOARD_POSITION[0], y=SCOREBOARD_POSITION[1])
        self.write(f"{self.p2score}", align="center", font=(FONT, FONT_SIZE, "normal"))

    def update_score(self, player):
        if player == 1:
            self.p1score += 1
        else:
            self.p2score += 1
        self.clear()
        self.write_score()
