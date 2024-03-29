from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.d_x = 20
        self.d_y = 0

        for i in range(3):
            (self.add_new_piece(- 20 * i, 0))

    def make_snake(self):
        for piece in self.snake_body:
            piece.reset()
        self.snake_body = []
        for i in range(3):
            (self.add_new_piece(- 20 * i, 0))

    def head(self):
        return self.snake_body[0]

    def add_new_piece(self, x, y):
        piece = Turtle("square")
        piece.color("white")
        piece.up()
        piece.goto(x=x, y=y)
        piece.speed("fastest")
        self.snake_body.append(piece)

    def add_new_segment(self):
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.add_new_piece(x, y)

    def move(self):
        # putting the last element at the head
        self.snake_body[-1].goto(self.snake_body[0].xcor() + self.d_x,
                                 self.snake_body[0].ycor() + self.d_y)
        self.snake_body.insert(0, self.snake_body.pop())

    def up(self):
        if self.d_y != -20:
            self.d_x = 0
            self.d_y = 20

    def down(self):
        if self.d_y != 20:
            self.d_x = 0
            self.d_y = -20

    def left(self):
        if self.d_x != 20:
            self.d_x = -20
            self.d_y = 0

    def right(self):
        if self.d_x != - 20:
            self.d_x = 20
            self.d_y = 0
