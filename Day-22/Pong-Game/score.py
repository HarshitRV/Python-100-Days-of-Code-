from turtle import Turtle, update

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.ht()
        self.penup()
        self.draw_line()
        self.color("white")
        self.update_score()
    
    def draw_line(self):
        self.goto(0, 300)
        self.pendown()
        self.seth(270)
        for _ in range(40):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

        self.penup()
    
    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(-100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
    
    def add_score(self,player):
        if player == "left":
            self.r_score += 1
            self.update_score()
        if player == "right":
            self.l_score += 1
            self.update_score()
    
    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))