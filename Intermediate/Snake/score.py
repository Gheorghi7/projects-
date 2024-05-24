from turtle import Turtle
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', mode='r') as read:
            self.high_score = int(read.read())
        self.up()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", align='center', font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as wr:
                wr.write(f"{self.score}")

        self.score = 0
        self.scoreboard()

    def increase_score(self):
        self.score += 1
        self.scoreboard()

