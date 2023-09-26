from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.new_car()
        self.step = STARTING_MOVE_DISTANCE
        self.update_count = 0

    def new_car(self):
        car = Turtle("square")
        car.up()
        car.goto(300, randint(-250, 250))
        car.setheading(180)
        car.shapesize(1, 2)
        car.color(COLORS[randint(0, 3)])
        self.car_list.append(car)
        return car

    def update(self):
        self.move()
        self.update_count += 1
        if self.update_count == 6:
            self.new_car()
            self.update_count = 0

    def move(self):
        for car in self.car_list:
            car.forward(self.step)

    def speed_up(self):
        self.step += MOVE_INCREMENT
