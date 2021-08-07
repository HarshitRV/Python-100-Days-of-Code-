from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()

#sets the color to rgb values
colormode(255)

colour = ["red","green","brown","yellow","purple","lime","blue"]
# turtle.pensize(3)

turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

def draw_square():
    for _ in range(4):
        turtle.forward(-50)
        turtle.right(-90)
        
# draw_square()

def dotted_line():
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

# dotted_line()



def shapes():
    j = 3
    while j != 11:
        turtle.color(random.choice(colour))
        for _ in range(j):
            turtle.right(360/j)
            turtle.forward(75)

        j += 1

# shapes()



def random_walk(duration):
    direction = [0, 90, 180 ,270]
    for _ in range(duration):
        turtle.setheading(random.choice(direction))
        turtle.color(random_color())
        turtle.forward(20)

# random_walk(500)


def draw_circle(radius):   
    turtle.circle(radius)

# draw_circle(100)

def spirograph(space):
    for _ in range(int(360/space)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + space)

spirograph(2)

screen = Screen()
screen.exitonclick()

