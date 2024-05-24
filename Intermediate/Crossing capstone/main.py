import time
from turtle import Screen
from player import Player
from cars import Cars
from score import  Score


game = True

screen = Screen()
screen.title("Crossing Capstone Game")
screen.setup(600,600)

player = Player()
car = Cars()
score = Score()

screen.listen()
screen.onkey(player.move, 'Up')

while game:
    screen.update()

    car.create_cars()
    car.move()
    for car_det in car.cars:
        if player.distance(car_det) < 30:
            game = False
            score.game_over()
        if car_det.xcor()<-300:
            car.cars.remove(car_det)
            car_det.hideturtle()

    if player.ycor() > 290:
        score.incr_score()

    if player.is_edge():
        player.start_pos()
        car.increment_speed()



screen.exitonclick()