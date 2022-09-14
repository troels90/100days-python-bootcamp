from turtle import Turtle

FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self. color("yellow")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.comp_score = 0
        self.update_score()

    def p_score(self):
        self.player_score += 1
        self.update_score()

    def c_score(self):
        self.comp_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-60, 210)
        self.write(self.player_score, align="center", font=FONT)
        self.goto((60, 210))
        self.write(self.comp_score, align="center", font=FONT)