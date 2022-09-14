from turtle import Turtle, Screen

trylle = Turtle()
screen = Screen()

def move_forwards():
    trylle.forward(10)

def turn_clockwise():
    trylle.right(10)

def turn_counterclockwise():
    trylle.left(10)

def move_backwards():
    trylle.backward(10)

def reset_sketch():
    trylle.reset()

screen.listen()
screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "d", fun= turn_clockwise)
screen.onkey(key= "a", fun= turn_counterclockwise)
screen.onkey(key="s", fun= move_backwards)
screen.onkey(key="c", fun= reset_sketch)

screen.exitonclick()