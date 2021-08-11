from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.pace = 0.1
    
    def move(self):
        self.goto((self.xcor() - self.x_move), (self.ycor() - self.y_move))
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.pace *= 0.9
    
    def reset_ball(self):
        self.goto(0, 0)
        self.pace = 0.1
        self.bounce_x()