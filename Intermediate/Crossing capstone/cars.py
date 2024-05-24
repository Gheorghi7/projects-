from turtle import Turtle
import random
SPEED = 20
MOVE_INCR = 10


class Cars():
    def __init__(self):
        self.cars = []
        self.speed = SPEED

    def create_cars(self):
        rand_chance = random.randint(1,2)
        if rand_chance == 1:
            tim = Turtle('square')
            Turtle.hideturtle(tim)
            tim.shapesize(1, 2)
            y = random.randrange(-300, 300, 20)
            tim.up()
            tim.goto(310, y)
            tim.showturtle()
            self.cars.append(tim)

    def move(self):
        for i in self.cars:
            i.backward(self.speed)

    def increment_speed(self):
        self.speed += MOVE_INCR


