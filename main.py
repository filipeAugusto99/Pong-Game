from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


scr.listen()
scr.onkey(r_paddle.up, "Up")
scr.onkey(r_paddle.down, "Down")
scr.onkey(l_paddle.w_key, "w")
scr.onkey(l_paddle.s_key, "s")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.07)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detect when r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.x_move = 10
        ball.y_move = 10
        scoreboard.l_point()

    # Detect when l paddle misess
    if ball.xcor() < -380:
        ball.reset_position()
        ball.x_move = 10
        ball.y_move = 10
        scoreboard.r_point()


scr.exitonclick()

