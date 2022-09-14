from turtle import Turtle

TEXT_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-215,260)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=TEXT_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=TEXT_FONT)