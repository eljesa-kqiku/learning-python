from turtle import colormode
from random import *


def random_color():
    colormode(255)
    return (randint(0, 255),
            randint(0, 255),
            randint(0, 255))