from turtle import Turtle

class Playground(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_boundry()

    def draw_boundry(self):
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.seth(270)
        self.pendown()
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()