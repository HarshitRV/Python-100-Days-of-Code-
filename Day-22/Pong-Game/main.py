from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from playground import Playground
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
playground = Playground()

game_is_on = True
def game_over():
    global game_is_on
    scoreboard.end_game()
    game_is_on = False

screen.listen()
screen.onkeypress(right_paddle.go_up,"w")
screen.onkeypress(right_paddle.go_down,"s")
screen.onkeypress(left_paddle.go_up,"Up")
screen.onkeypress(left_paddle.go_down,"Down")
screen.onkeypress(game_over,"x")


while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # detect if ball went out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.add_score('left')
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.add_score('right')
    
screen.exitonclick()