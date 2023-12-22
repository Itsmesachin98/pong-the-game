from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.r_score = 0
        self.l_score = 0
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.turtle.clear()
        self.turtle.goto(100, 180)
        self.turtle.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.turtle.goto(-100, 180)
        self.turtle.write(self.l_score, align="center", font=("Courier", 80, "normal"))


    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()


    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()