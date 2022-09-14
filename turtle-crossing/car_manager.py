from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_Y_START_POSITION = [240,220,200,180,160,140,120,100,80,60,40,20,0,
                        -20,-40,-60,-80,-100,-120,-140,-160,-180,-200,-220,-240,-240]
X_START = 290

class CarManager():
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(0.8, 1.5, 0)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(X_START, random.choice(CAR_Y_START_POSITION))
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.car_speed)

    def collision_check(self,player):
        player_x = player.xcor()
        player_y = player.ycor()
        for car in self.cars_list:
            if car.distance(player_x, player_y) < 15:
                return True
        return False

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def clear_list(self):
        ### Clear all cars that have driven through
        for i in range(0, len(self.cars_list)-5):
            car = self.cars_list[i]
            if car.xcor() > -305:
                self.cars_list = self.cars_list[i:]
                break









