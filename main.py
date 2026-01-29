from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


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
        ball.bounce()

    # elif ball.distance(r_paddle) < 50:
    #     dy *= 1
    #     dx = -10
    #     dy = -10
    #
    # elif ball.distance(l_paddle) < 50:
    #     dx = 10
    #     dy = 10
    #
    # ball.move(dx, dy)

scr.exitonclick()

