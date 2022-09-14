import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    ### Detect food collision
    if snake.head.distance(food) < 15:
        print("check")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    ### Detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #### Detect tail collision
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 15:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
