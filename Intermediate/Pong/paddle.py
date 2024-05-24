from turtle import Turtle
SPEED = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddl()

    def create_paddl(self):
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.up()
        self.goto(370, 0)

    def move_up_r(self):
        new_y = self.ycor() + SPEED
        self.goto(370, new_y)

    def move_down_r(self):
        new_y = self.ycor() - SPEED
        self.goto(370, new_y)
