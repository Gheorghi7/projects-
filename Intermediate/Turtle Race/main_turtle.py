import random
from turtle import Turtle, Screen


color = ['purple', 'green', 'red', 'blue', 'orange']
y_pos = [200, 100, 0, -100, -200]
turtle_bots = []

screen = Screen()
game = False

user_bet = screen.textinput('Make your bet', 'which turtle will win the race? Enter a color: ')
print(user_bet)

screen.setup(900, 600)

for index in range(0, 5):
    tim = Turtle(shape='turtle')
    tim.color(color[index])
    tim.up()
    tim.goto(-430, y_pos[index])
    turtle_bots.append(tim)

if user_bet:
    game = True

while game:
    for turtle in turtle_bots:
        if turtle.xcor() > 430:
            game = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You`ve win {winning}")
            else:
                print(f"You lost, winner {winning}")
        rand = random.randint(0, 10)
        turtle.forward(rand)

screen.exitonclick()
