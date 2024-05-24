import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from paddle_bot import PaddleBot
from score import Score

screen = Screen()
paddle = Paddle()
paddle_bot = PaddleBot()
ball = Ball()
score = Score()


game = True


screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Pong")


screen.listen()
screen.onkey(paddle.move_up_r, 'Up')
screen.onkey(paddle_bot.move_up_l, 'w')
screen.onkey(paddle.move_down_r, 'Down')
screen.onkey(paddle_bot.move_down_l, 's')


while game:
    screen.update()
    time.sleep(0.1)
    score.score_b()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 350 or ball.distance(paddle_bot) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score.increase_l_score()
    elif ball.xcor() < -400:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        score.increase_r_score()

    if score.r_score > 10 or score.l_score > 10:
        score.end()
        game = False


screen.exitonclick()
