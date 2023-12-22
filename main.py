from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.title("Pong The Game")
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# Defining class
r_paddle = Paddle(460, 0)
l_paddle = Paddle(-460, 0)
ball = Ball(0, 0)
scoreboard = Scoreboard()

# Listening to keystrokes
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collison when the ball hits the upper and lower wall
    if ball.y_cor > 280 or ball.y_cor < -280:
        ball.bounce_y()

    # Detect collison when the ball hits the paddle
    if ball.turtle.distance(r_paddle.turtle) < 50 and ball.x_cor > 440:
        ball.bounce_x()

    if ball.turtle.distance(l_paddle.turtle) < 50 and ball.x_cor < -440:
        ball.bounce_x()

    # Detect when the ball goes out of bounds
    if ball.x_cor > 480:
        ball.reset_position()
        scoreboard.update_l_score()

    elif ball.x_cor < -480:
        ball.reset_position()
        scoreboard.update_r_score()

# Exit screen
screen.exitonclick()