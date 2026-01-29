from turtle import Turtle


MOVE_DISTANCE = 30
x_pos = 350
y_pos = 0

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)


    def create_paddle(self, pos):
            self.penup()
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
            self.color("white")
            self.goto(pos)
            return self

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def w_key(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def s_key(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
