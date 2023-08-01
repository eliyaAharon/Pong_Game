from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.l_score = 0
        self.r_score = 0
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.color("red")
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.color("blue")
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def l_point(self):
        self.l_score += 1
        self.display()

    def r_point(self):
        self.r_score += 1
        self.display()
