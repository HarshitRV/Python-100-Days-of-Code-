from turtle import Turtle, Screen, color
import turtle
import random

screen = Screen()

# Allow to setup width and height of the screen
screen.setup(width=500, height=400)

refree_turtle = Turtle(shape="turtle")
refree_turtle.setheading(90)
refree_turtle.penup()
refree_turtle.goto(218, -200)
refree_turtle.pendown()
refree_turtle.goto(218, 200)

race_on = False
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race").lower()


color = ["red", "orange", "blue", "purple", "green", "yellow"]
y_position = [-80, -50, -20, 10, 40, 70]
turtle_list = []

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(color[i])
    turtle.penup()
    turtle.goto(-230,y_position[i])
    turtle_list.append(turtle)

if bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 218:
            winner = turtle.pencolor()
            race_on = False

        turtle.fd(random.randint(0, 10))

if bet == winner:
    print("Your turtle won the race")
else:
    print(f"You Lost. The winner is {winner} turtle")

screen.exitonclick()