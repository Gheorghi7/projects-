from turtle import Turtle
SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.hideturtle()
        self.shape('turtle')
        self.up()
        self.left(90)
        self.start_pos()
        self.showturtle()

    def move(self):
        self.forward(SPEED)

    def start_pos(self):
        self.hideturtle()
        self.goto(0, -280)
        self.showturtle()

    def is_edge(self):
        if self.ycor() > 290:
            return True
        else:
            return False
