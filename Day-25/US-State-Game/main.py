from turtle import Turtle, Screen
import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = Screen()
turtle = Turtle()
turtle_write = Turtle()

screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
correct = 0
guessed_states = []
while game_is_on and correct != 50:
    state_name = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state name?").title()
    states_list = data.state.to_list()

    #Exit from the game
    if state_name == "Exit":
        missed_state = [state for state in states_list if state not in guessed_states] # List comprehension
        states_to_learn = {
            "To Learn": missed_state
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
        turtle_write.goto(state_cordinates)
        turtle_write.write(f"{state_name}" ,move="false", align="center", font=("Helvetica", 7, "bold"))
        correct += 1

# turtle.getscreen()._root.mainloop()