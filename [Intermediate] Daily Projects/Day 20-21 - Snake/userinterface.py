from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class UserInterface:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600,height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)