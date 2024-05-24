from turtle import Turtle, Screen
import time
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self,pos):
        tim = Turtle('square')
        tim.speed(0)
        tim.color('white')
        tim.up()
        tim.goto(pos)
        self.segment.append(tim)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(2000,2000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def move(self):
        screen.update()
        time.sleep(0.1)
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
