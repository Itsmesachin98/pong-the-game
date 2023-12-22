from turtle import Turtle

class Ball:
    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.turtle = Turtle("square")
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.shapesize(1, 1)
        self.turtle.speed("fastest")

    # Make the ball move
    def move(self):
        self.x_cor = self.turtle.xcor() + self.x_move
        self.y_cor = self.turtle.ycor() + self.y_move
        self.turtle.goto(self.x_cor, self.y_cor)

    # When ball hits the wall
    def bounce_y(self):
        self.y_move *= -1

        
    # When ball hits the paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Reset the ball position
    def reset_position(self):
        self.turtle.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
