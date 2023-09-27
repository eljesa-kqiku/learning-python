from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    scoreboard.update()

    # Detect collision with food
    if snake.head().distance(food) < 20:
        scoreboard.add_point()
        food.move()
        snake.add_new_segment()

    # Detect collision with borders
    if not snake.head().xcor() in range(-300, 301) or not snake.head().ycor() in range(-300, 301):
        scoreboard.reset()
        snake.make_snake()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head().distance(segment) < 10:
            scoreboard.reset()
            snake.make_snake()


screen.exitonclick()
