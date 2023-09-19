from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def move_forwards():
    pen.forward(10)


screen.listen()
screen.onkey(move_forwards, 'space')
screen.exitonclick()