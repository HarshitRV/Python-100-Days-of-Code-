import random
from turtle import Turtle, Screen, colormode
import colorgram

turtle = Turtle()
screen = Screen()
colormode(255)
turtle.speed("fastest")
turtle.ht()

# Setting the starting position for turtle
HOME = (-275, -325)
turtle.penup()
turtle.goto(HOME)
turtle.pendown()

rgb_color = []
colors = colorgram.extract("images.jfif", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print(rgb_color)

# Brings turtle back to starting position
def level_up(up_by):
    global HOME

    turtle.penup()
    turtle.goto(HOME)
    turtle.setheading(90)
    turtle.forward(up_by)
    turtle.setheading(0)
    turtle.pendown()


def hirst_painting(radius):
    up = 0
    for _ in range(10):
        for _ in range(10):
            turtle.dot(radius, random.choice(rgb_color))
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()

        up += 50
        level_up(up)


hirst_painting(20)


screen.exitonclick()
