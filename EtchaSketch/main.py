from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.listen()


def move_right():
    pen.right(90)
    pen.forward(10)


def move_left():
    pen.left(90)
    pen.forward(10)


def clear():
    pen.up()
    pen.home()
    pen.clear()
    pen.down()


def move_forward():
    pen.forward(10)


def move_back():
    pen.backward(10)


screen.onkey(move_forward, 'w')
screen.onkey(move_back, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()