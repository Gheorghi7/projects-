from turtle import Turtle
SPEED = 20


class PaddleBot(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddl()

    def create_paddl(self):
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.up()
        self.goto(-370, 0)

    def move_up_l(self):
        new_y = self.ycor() + SPEED
        self.goto(-370, new_y)

    def move_down_l(self):
        new_y = self.ycor() - SPEED
        self.goto(-370, new_y)
