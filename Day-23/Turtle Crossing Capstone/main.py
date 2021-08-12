from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = Car()
score = Scoreboard()

game_is_on = True
def game_over():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkey(game_over, "x")
screen.onkey(player.move_player, "w")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.car_move()

    # detect the collision of turtle with car
    for car in cars.all_cars:
        if player.distance(car) < 30:
            score.end_game()
            game_is_on = False
    
    #level up each time turtle reaches top and increase difficulty
    if player.ycor() > 280:
        score.level_up()
        player.goto(0, -280)
        cars.speed_on_level_up()

screen.exitonclick()