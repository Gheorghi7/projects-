import time
from turtle import Screen
from snake import Snake
from snake_food import Food
from score import Score

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor('black')
screen.title('Snake Game')

game = True
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
