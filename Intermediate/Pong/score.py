from turtle import Turtle
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.up()
        self.hideturtle()
        self.goto(0, 260)

    def score_b(self):
        self.write(f"{self.l_score}:{self.r_score}", align='center', font=FONT)

    def end(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.score_b()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.score_b()
