from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,paddle_pos):
        super().__init__()
        self.penup()
        self.goto(paddle_pos)
        self.color('white')
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(),y_cor)
        
    def go_down(self):
        y_cor = self.ycor() -20
        self.goto(self.xcor(), y_cor)