from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.speed("fastest")

def move_forwards():
    turtle.fd(5)

def move_backwards():
    turtle.bk(5)


def counter_clockwise():
    head = turtle.heading() + 10
    turtle.setheading(head)

def clockwise():
    head = turtle.heading() - 10
    turtle.setheading(head)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.setheading(0)

screen.listen()
screen.onkey(key='w',fun=move_forwards)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear_screen)

screen.exitonclick()