import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
y_position = [125, 75, 25, -25, -75, -125]
colors = ["red", "green", "purple", "orange", "blue", "yellow"]
screen = Screen()
user_bet = screen.textinput("Make your bet", "Who is gonna win!?: ").lower()
all_turtles = []
screen.setup(width=500, height=400)


for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win. {winning_color} is the winner! ")
            else:
                print(f"The winner is {winning_color}. You lost")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)







screen.exitonclick()