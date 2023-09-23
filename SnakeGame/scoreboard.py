from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.update()
        self.setposition(0, 270)

    def add_point(self):
        self.points += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.points}", False,
                   align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over!", False,
                   align="center", font=("Arial", 15, "normal"))
