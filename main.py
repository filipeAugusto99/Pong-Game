from turtle import Screen
from paddle import Paddle

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

paddle = Paddle()

scr.listen()
scr.onkeypress(paddle.up, "Up")
scr.onkeypress(paddle.down, "Down")

game_is_on = True
while game_is_on:
    scr.update()



scr.exitonclick()

