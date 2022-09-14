from turtle import Turtle
ALIGNMENT = "center"
FONT= ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", False, ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over", False, ALIGNMENT, font=FONT)

    def save_high_score(self):
        with open("highscore.txt", mode="w") as file:
            file.write(f"{self.score}")

    def load_high_score(self):
        with open("highscore.txt") as file:
            highscore = file.read()

        return int(highscore)