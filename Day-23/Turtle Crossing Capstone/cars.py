from turtle import Turtle
import random

INITIAL_SPEED = 5
INCREMENT = 10


COLORS = ["red", "orange", "blue", "purple", "green", "yellow"]

class Car():
    def __init__(self):
        self.all_cars = []
        self.initial_speed = INITIAL_SPEED
    
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
            car.fd(self.initial_speed)
    
    def speed_on_level_up(self):
        self.initial_speed += INCREMENT
