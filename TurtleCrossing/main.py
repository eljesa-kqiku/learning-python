import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.update()

    # Detect collision with cars
    for car in car_manager.car_list:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Game won
    if player.ycor() >= 270:
        player.restart()
        car_manager.speed_up()
        scoreboard.update()

screen.exitonclick()
