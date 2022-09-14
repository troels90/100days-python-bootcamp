import random
from turtle import Turtle

BALL_SPEED = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collide(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def wall_collide(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1
        self.move_speed = 0.1


