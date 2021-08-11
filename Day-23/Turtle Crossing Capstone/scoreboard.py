from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.ht()
        self.goto(-270, 270)
        self.write(f"Level : {self.level}" ,align="left", font=("Courier", 15, "normal"))
    
    def level_up(self):
        self.clear()
        self.level +=1
        self.write(f"Level : {self.level}" ,align="left", font=("Courier", 15, "normal"))
    
    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over" ,align="center", font=("Courier", 15, "bold"))
