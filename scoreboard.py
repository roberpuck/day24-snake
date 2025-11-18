from importlib.resources import contents
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score_file:
            self.high_score = high_score_file.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open('data.txt',mode='w') as high_score_file:
                high_score_file.write(str(self.score))
            self.high_score = self.score
        self.score =0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
