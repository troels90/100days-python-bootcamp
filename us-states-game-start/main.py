import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES")
data = pandas.read_csv("50_states.csv")
print(data)
all_states = data.state.to_list()
print(all_states)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="Name a state: ").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_obj = turtle.Turtle()
        state_obj.penup()
        state_obj.hideturtle()
        state_data = data[data.state == answer_state]
        state_obj.goto(int(state_data.x), int(state_data.y))
        state_obj.write(answer_state, align="center")


# screen.exitonclick()