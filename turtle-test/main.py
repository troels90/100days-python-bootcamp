import turtle
from turtle import Turtle, Screen
import heroes
import random

PI = 3.14159
tim = Turtle()
tim.shape("arrow")
tim.speed(5)

colours = ["red", "blue", "green", "blue violet", "royal blue"]
tim.pensize(1)
directions = [0, 90, 180, 270]


def random_walk():
    tim.setheading(random.choice(directions))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(colours))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# for i in range (0,36):
#     tim.left(10)
#     tim.circle(100)
    # for move in range(0,120):
    #         tim.forward(movement)
    #         angle = 3
    #         print(move)
    #         tim.left(angle)

# def random_walk():
#     angle = random.randint(0,3)
#     print(angle)
#     if angle == 1:
#         tim.left(90)
#     elif angle == 2:
#         tim.right(90)
#     elif angle == 3:
#         tim.right(180)
#     elif angle == 0:
#         tim.right(0)


# def draw_shapes(num_sides):
#     angle = (360 / num_sides)
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for _ in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shapes(_)

my_screen = Screen()
my_screen.exitonclick()
