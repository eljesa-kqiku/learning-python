import random
from turtle import Turtle, Screen

space = 30
start = 3 * space
screen = Screen()
screen.setup(width=500, height=400)
user_winner = screen.textinput(title="Make your bet", prompt="Which turtle do you think is going to win? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
all_turtles = []

for i in range(7):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.up()
    turtle.goto(x=-230, y=start - i * space)
    all_turtles.append(turtle)

game_on = True
finish_line = 230
while game_on:
    for turtle in all_turtles:
        if game_on:
            step = random.randint(0, 10)
            turtle.forward(step)
            if turtle.pos()[0] >= finish_line:
                game_on = False
                if turtle.pencolor() == user_winner:
                    print("You won")
                else:
                    print("You lost")
                print(f"Winner {turtle.pencolor()}")

# if winners.__contains__(us)





screen.exitonclick()
