import turtle
import pandas
from output import Pen

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
all_states = pandas.read_csv("50_states.csv")
pen = Pen()

guessed_states = []
data = all_states.state.tolist()
while len(guessed_states) < 50:
    state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States", prompt="What's another state's name?: ")
    state = state.title()
    if state == 'Exit':
        missing_states = [state for state in data if state not in guessed_states]
        data_to_save = pandas.DataFrame({"missing_states": missing_states})
        data_to_save.to_csv("states_to_learn.csv")
        break

    state_data = all_states[all_states.state == state]
    if not state_data.empty and state not in guessed_states:
        pen.write_state(state, int(state_data.x.item()), int(state_data.y.item()))
        guessed_states.append(state)
