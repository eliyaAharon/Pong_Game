from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("circle")
        self.x_move = 1.0
        self.y_move = 1.0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart_ball(self):
        self.goto(0, 0)
        self.x_move = 1
        self.y_move = 1
        self.x_move *= -1

    def increase_speed(self):
        if self.x_move < 4:
            self.x_move *= 1.1
            self.y_move *= 1.1
