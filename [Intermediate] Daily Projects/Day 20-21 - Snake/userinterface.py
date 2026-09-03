from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Ithaca", 24, "normal")

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
        self.current_highscore = 0
        self.get_highscore()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt", "r") as file:
            self.current_highscore = file.read()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}    High Score: {self.current_highscore}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)
        if self.score > int(self.current_highscore):
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))