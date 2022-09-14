from turtle import Turtle

UPPER_Y = 280
LOWER_Y = -280
RIGHT_X = 405
LEFT_X = -405

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("yellow")
        self.hideturtle()

    def draw_field(self):
        self.draw_middle()
        self.draw_upper()
        self.draw_lower()

    def draw_middle(self):
        self.goto(0, LOWER_Y)
        self.setheading(90)
        while self.ycor() < UPPER_Y:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.penup()

    def draw_upper(self):
        self.goto(RIGHT_X,UPPER_Y)
        self.pendown()
        self.goto(LEFT_X, UPPER_Y)
        self.penup()

    def draw_lower(self):
        self.goto(410,-280)
        self.pendown()
        self.goto(-410,-280)
        self.penup()