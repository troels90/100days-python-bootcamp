from paddle import Paddle

PLAYER_START = (-380, 0)
class Player(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(PLAYER_START)
        self.forward(20)

    def up(self):
        if self.ycor() > 220:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() < -220:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
