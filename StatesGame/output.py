from turtle import Turtle

FONT = ("Arial", 8, "normal")


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state, x, y):
        self.setposition(x, y)
        self.write(state, False, align="center", font=FONT)
