from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

screen.listen()
screen.tracer(0)

paddle_r = Paddle((SCREEN_WIDTH / 2 - 50, 0))
paddle_l = Paddle((-SCREEN_WIDTH / 2 + 50, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
scoreboard.update()

# Draw middle line
pen = Turtle()
pen.color("white")
pen.pensize(5)
pen.up()
pen.goto(0, SCREEN_HEIGHT / 2)
pen.down()
pen.setheading(270)
for _ in range(SCREEN_HEIGHT // 20):
    pen.forward(10)
    pen.up()
    pen.forward(10)
    pen.down()

screen.update()

game_on = True
while game_on:
    time.sleep(ball.sleep_time)
    ball.move()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() >= SCREEN_HEIGHT / 2 - 20 or ball.ycor() <= -SCREEN_HEIGHT / 2 + 20:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() >= SCREEN_WIDTH / 2 - 80
            or ball.distance(paddle_l) < 50 and ball.xcor() <= -SCREEN_WIDTH / 2 + 80):
        ball.bounce_x()

    # Detect right paddle miss
    elif ball.xcor() > SCREEN_WIDTH / 2 - 20:
        ball.restart()
        scoreboard.add_score_l()

    # Detect left paddle miss
    elif ball.xcor() < - SCREEN_WIDTH / 2 + 20:
        ball.restart()
        scoreboard.add_score_r()

screen.exitonclick()
