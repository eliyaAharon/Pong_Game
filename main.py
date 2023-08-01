from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# screen settings.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddle set.
paddle_1 = Paddle(1)
paddle_2 = Paddle(2)

# screen keys control
screen.listen()
# user 1's keys.
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
# user 2's keys.
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

# ball set
ball = Ball()
scoreboard = Scoreboard()

is_game_on = True

while is_game_on:


    screen.update()
    ball.move()
    # check collision with the top & the bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # check collision with the paddles
    if ball.distance(paddle_1) < 50 and ball.xcor() > 340 or ball.distance(paddle_2) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.increase_speed()
    # check paddle miss.
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart_ball()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart_ball()
screen.exitonclick()
