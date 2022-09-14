from paddle import Paddle

COMPUTER_START = (360, 0)

class Computer(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(COMPUTER_START)

    # AI skal altid rykke tilbage mod midten, når bolden er halvejs tilbage rykker den mod boldens y
    def move(self, ball):
        if ball.xcor() < 0 and ball.x_move < 0:
            if self.ycor()< 10:
                self.up()
            elif self.ycor() > 0:
                self.down()
            elif 0 < self.ycor() < 9:
                pass
        if ball.xcor() > 0:
            if ball.ycor() > 10 or ball.ycor() < self.ycor():
                self.up()
            elif ball.ycor() < 0 or ball.ycor() > self.ycor():
                self.down

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