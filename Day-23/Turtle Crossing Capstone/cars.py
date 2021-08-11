from turtle import Turtle
import random


COLORS = ["red", "orange", "blue", "purple", "green", "yellow"]

class Car():
    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        if random.randint(1,6) == 3:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.seth(180)
            car.goto(300, random.randint(-240,240))
            self.all_cars.append(car)
    
    def car_move(self):
        for car in self.all_cars:
            car.fd(10)
