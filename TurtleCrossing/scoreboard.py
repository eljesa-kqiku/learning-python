import turtle
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.setposition(-280, 250)
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over!", False, align="center", font=FONT)