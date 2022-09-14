###Create a screen, create a paddle and move, ball physics, collision, paddle
import time
from ball import Ball
from field import Field
from player import Player
from turtle import Screen
from compai import Computer
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
field = Field()
field.draw_field()
player = Player()
computer = Computer()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.down, "s")
screen.onkeypress(player.up, "w")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(player) < 50 and ball.xcor() < - 330 or ball.distance(computer) < 50 and ball.xcor() > 340:
        ball.collide()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_collide()

    if ball.xcor() > 390:
        ball.reset()
        scoreboard.p_score()
    elif ball.xcor() < -390:
        ball.reset()
        scoreboard.c_score()

    computer.move(ball)


screen.exitonclick()