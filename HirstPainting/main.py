# import colorgram
from turtle import Turtle, Screen, colormode, screensize
from random import randint
# colors = colorgram.extract('image.jpg', 30)
# palette = []
# for color in colors:
#     palette.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(palette)

# after extracting the colors we have this palette

palette = [(240, 228, 200), (213, 239, 225), (209, 227, 241), (242, 216, 232), (209, 158, 113), (228, 216, 111), (122, 173, 204), (205, 136, 171), (124, 189, 158), (206, 78, 129), (56, 100, 152), (229, 167, 195), (162, 60, 110), (152, 215, 188), (179, 14, 60), (153, 86, 57), (141, 212, 225), (59, 172, 132), (212, 88, 69), (31, 171, 200), (234, 171, 160), (106, 111, 181), (178, 182, 224), (61, 121, 90), (172, 155, 55), (43, 48, 121), (25, 35, 72), (68, 19, 48), (168, 18, 10), (17, 57, 33)]


def random_color():
    rand_index = randint(0, len(palette) - 1)
    return palette[rand_index]


# set up config variables
space = 15
dot_radius = 15
num_dots = 10

# calculate other variables
step = space + dot_radius * 2
dot_diameter = dot_radius * 2
screen_size = (dot_diameter + space) * num_dots + 5 * space

# setup Tutle 
pen = Turtle()
colormode(255)
screensize(screen_size, screen_size)
pen.up()
pen.hide()
pen.setposition(-screen_size / 2 + 2 * space, - screen_size / 2 + 2 * space)

for i in range(num_dots):
    if i != 0:
        if i % 2 == 1:
            pen.left(90)
            pen.fd(step)
            pen.left(90)
        else:
            pen.right(90)
            pen.fd(step)
            pen.right(90)

    for j in range(num_dots):
        if j != 0:
            pen.fd(step)
        pen.dot(dot_diameter, random_color())

scene = Screen()
scene.exitonclick()
