from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
        def __init__(self):
            super().__init__()
            self.penup()
            self.shape("turtle")
            self.color("green")
            self.setheading(90)
            self.goto(STARTING_POSITION)
            self.goal = FINISH_LINE_Y

        def up(self):
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

        def left(self):
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

        def right(self):
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

        def got_hit(self):
            self.shape("circle")
            self.color("red")

        def finish_line(self):
            self.goto(STARTING_POSITION)
