from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(0, -280)
        self.seth(90)

    def move_player(self):
        self.fd(10)