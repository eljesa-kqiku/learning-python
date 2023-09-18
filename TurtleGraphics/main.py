from random import randint
from turtle import Turtle, Screen, colormode


def draw_star():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("DarkGoldenrod1")
    timmy.penup()
    timmy.setpos(-225, 50)
    timmy.pendown()

    timmy.forward(500)
    timmy.right(150)

    timmy.forward(450)
    timmy.right(140)

    timmy.forward(400)
    timmy.right(140)

    timmy.forward(400)
    timmy.right(140)
    timmy.forward(450)

    my_screen = Screen()
    print(my_screen.canvwidth)
    my_screen.exitonclick()


def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.left(90)


def draw_dashed_line():
    for _ in range(10):
        pen.forward(5)
        pen.up()
        pen.forward(5)
        pen.down()


def random_color():
    colormode(255)
    return (randint(0, 255),
            randint(0, 255),
            randint(0, 255))


def draw_polygons():
    side_length = 80
    start_polygon = 3  # triangle
    max_polygon = 10  # decagon

    for polygon in range(start_polygon, max_polygon + 1):
        angle = 360 / polygon
        pen.color(random_color())
        for side in range(polygon):
            pen.forward(side_length)
            pen.right(angle)


def random_walk():
    pen.ht()
    pen.width(15)
    pen.speed("fastest")
    step = 30

    for _ in range(200):
        angle = 90 * randint(0, 3)
        pen.color(random_color())
        pen.setheading(angle)
        pen.forward(step)


def draw_spirograph():
    radius = 100
    density = 50
    angle = 360 / density
    pen.hideturtle()
    pen.speed("fastest")
    for i in range(density):
        pen.color(random_color())
        pen.right(angle)
        pen.circle(radius)


# initialization
pen = Turtle()
pen.shape("arrow")
pen.color("black")
pen.shapesize(0.5, 0.5)

# function call
draw_spirograph()

# screen controls
screen = Screen()
screen.exitonclick()
