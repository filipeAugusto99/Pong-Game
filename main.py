from turtle import Screen
from paddle import Paddle

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


scr.listen()
scr.onkey(r_paddle.up, "Up")
scr.onkey(r_paddle.down, "Down")
scr.onkey(l_paddle.w_key, "w")
scr.onkey(l_paddle.s_key, "s")

game_is_on = True
while game_is_on:
    scr.update()



scr.exitonclick()

