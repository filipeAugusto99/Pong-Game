from turtle import Turtle

MOVE_DISTANCE = 30
PADDLES_POSITIONS = [(350, 0), (-350, 0)]
x_pos = 350
y_pos = 0

class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()

    def create_paddle(self):

        for position in PADDLES_POSITIONS:
            new_paddle = Turtle()
            new_paddle.speed("fastest")
            new_paddle.penup()
            new_paddle.shape("square")
            new_paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)
            new_paddle.color("white")
            new_paddle.goto(position)
            self.paddles.append(new_paddle)

    def up(self):
        if self.paddles[1].ycor() < 250:
            self.paddles[1].sety(self.paddles[1].ycor() + MOVE_DISTANCE)

    def down(self):
        if self.paddles[1].ycor() > -250:
            self.paddles[1].sety(self.paddles[1].ycor() - MOVE_DISTANCE)