from turtle import Turtle

class Paddle:
    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.turtle = Turtle("square")
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.shapesize(5, 1)
        self.turtle.goto(x_cor, y_cor)


    def move_up(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor() + 20)


    def move_down(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor() - 20)