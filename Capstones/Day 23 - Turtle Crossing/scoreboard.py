from turtle import Turtle
FONT = ("Ithaca", 30, "normal")
SCOREBOARD_LOCATION = (-245, 240)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(SCOREBOARD_LOCATION)
        self.write(f"level: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER", align="center", font=FONT)