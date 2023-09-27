from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("blue")
        self.move()

    def move(self):
        x = randint(-14, 14) * 20
        y = randint(-14, 14) * 20
        self.goto(x, y)
