from turtle import Turtle, position

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {self.score}", move=True, align="center", font=("Arial", 12, "bold"))
    
    def points(self):
        self.clear()
        self.goto(0,280)
        self.write(f"Score: {self.add_points()}", move=True, align="center", font=("Arial", 12, "bold"))
    
    def add_points(self):
        self.score += 1
        return self.score
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=True, align="center", font=("Arial", 12, "bold"))