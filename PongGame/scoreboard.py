from turtle import Turtle

FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color("white")

        self.score_l = 0
        self.score_r = 0

    def add_score_r(self):
        self.score_r += 1
        self.update()

    def add_score_l(self):
        self.score_l += 1
        self.update()

    def update(self):
        self.clear()

        self.goto(-100, 250)
        self.write(f"{self.score_l}", False,
                   align="center", font=FONT)

        self.goto(100, 250)
        self.write(f"{self.score_r}", False,
                   align="center", font=FONT)
