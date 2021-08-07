from turtle import Turtle, Screen
import random

turtle = Turtle()


colour = ["red","green","brown","yellow","purple","lime","blue"]

def draw_square():
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
        
# draw_square()

def dotted_line():
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

# dotted_line()

def shapes():
    turtle.color(colour[0])
    for _ in range(4):
        turtle.forward(75)
        turtle.right(90)
        
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()

    i = 1
    j = 5

    while j != 11:
        turtle.color(colour[i])
        for _ in range(j):
            turtle.right(360/j)
            turtle.forward(75)

        i += 1
        j += 1

shapes()

screen = Screen()
screen.exitonclick()

