from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0

        self.high_score = 0
        self.read_highest_score()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()
        self.setposition(0, 270)

    def add_point(self):
        self.points += 1
        if self.points > self.high_score:
            self.high_score = self.points
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", False,
                   align="center", font=("Arial", 10, "normal"))

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            self.save_highest_score()
        self.points = 0
        self.update()

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over!", False,
                   align="center", font=("Arial", 15, "normal"))

    def read_highest_score(self):
        with open('highest_score.txt') as file:
            score = file.read()
            if score:
                self.high_score = int(score)

    def save_highest_score(self):
        with open('highest_score.txt', mode='w') as file:
            file.write(str(self.high_score))
