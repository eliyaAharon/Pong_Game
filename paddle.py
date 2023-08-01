from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, user_num):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if user_num == 1:
            self.color("blue")
            self.goto(360, 0)
        elif user_num == 2:
            self.color("red")
            self.goto(-360, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
