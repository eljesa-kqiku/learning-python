from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(5, 1)
        self.penup()
        self.goto(start_pos)

    def move_up(self):
        y = self.ycor() + 25
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 25
        self.goto(self.xcor(), y)
