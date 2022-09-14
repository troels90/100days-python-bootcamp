from turtle import Turtle, Screen
import random
color_list = [(197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68), (228, 160, 47), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62)]

pen = Turtle()
pen.pensize(20)
pen.penup()
pen.hideturtle()
pen.setposition(-200,-200)

my_screen = Screen()
my_screen.colormode(255)

def draw():
    pen.pendown()
    pen.forward(1)
    pen.penup()

def u_turn_left():
    draw()
    pen.forward((50))
    pen.left(90)
    pen.forward((50))
    pen.left(90)
    pen.forward((50))

def u_turn_right():
    draw()
    pen.forward(50)
    pen.right(90)
    pen.forward((50))
    pen.right(90)
    pen.forward((50))

for y in range(0,10):
    for x in range(0,10):
        if x == 9 and y % 2 == 0:
            u_turn_left()
        elif x == 9 and y % 2 != 0:
            u_turn_right()
        else:
            pen.color(random.choice(color_list))
            draw()
            pen.forward(50)

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)


my_screen.exitonclick()
