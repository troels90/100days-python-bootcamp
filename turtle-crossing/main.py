import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    car_manager.create_cars()
    car_manager.move_cars()
    collision = car_manager.collision_check(player)
    if collision:
        game_is_on = False
        player.got_hit()
        scoreboard.game_over()
    if player.ycor() > player.goal:
        scoreboard.update_scoreboard()
        car_manager.clear_list()
        player.finish_line()
        car_manager.increase_speed()
    screen.update()


screen.exitonclick()