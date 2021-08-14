from turtle import Turtle, Screen
import turtle
import pandas

data = pandas.read_csv("states.csv")
screen = Screen()
screen.setup(800, 800)
turtle = Turtle()
turtle_write = Turtle()

screen.title("Indian States Game")
image = "indian_states.gif"
screen.addshape(image)
turtle.shape(image)


game_is_on = True
correct = 0
guessed_states = []
missed_state = []
while game_is_on and correct != 28:
    state_name = screen.textinput(title=f"{correct}/28 States Correct", prompt="What's another state name?").title()
    states_list = data.state.to_list()

    #Exit from the game
    if state_name == "Exit":
        for state in states_list:
            if state not in guessed_states:
                missed_state.append(state)

        states_to_learn = {
            "Missed States": missed_state
        }
        new_data = pandas.DataFrame(states_to_learn)
        save = screen.textinput(title="Need help?", prompt="Do you want the list of missed states?(y/n)").title()
        if save == "Y":
            new_data.to_csv("missed_states.csv")
        break

    # Check if the entered state is in the states_list
    if state_name in states_list:
        guessed_states.append(state_name)
        turtle_write.ht()
        turtle_write.penup()
        state_cordinates = (int(data[data.state == state_name].x), int(data[data.state == state_name].y))
        print(state_cordinates)
        turtle_write.goto(state_cordinates)
        turtle_write.write(f"{state_name}" ,move="false", align="center", font=("Helvetica", 7, "bold"))
        correct += 1
