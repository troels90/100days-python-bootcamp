from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def extend(self):
        self.add_part(self.parts[-1].position())

    def add_part(self, position):
        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(position)
        self.parts.append(new_box)

    def reset(self):
        for part in self.parts:
            part.goto(500,500)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]

    def move(self):
        for seg in range(len(self.parts) - 1, 0, -1):  # ( Start, Stop, Step)
            new_x = self.parts[seg - 1].xcor()
            new_y = self.parts[seg - 1].ycor()
            self.parts[seg].goto(new_x, new_y)
        self.parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.parts[0].heading() != DOWN:
            self.parts[0].setheading(UP)

    def down(self):
        if self.parts[0].heading() != UP:
            self.parts[0].setheading(DOWN)

    def left(self):
        if self.parts[0].heading() != RIGHT:
            self.parts[0].setheading(LEFT)

    def right(self):
        if self.parts[0].heading() != LEFT:
            self.parts[0].setheading(RIGHT)