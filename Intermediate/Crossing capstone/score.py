from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_table()

    def create_table(self):
        self.hideturtle()
        self.up()
        self.goto(210, 260)
        self.write(f"Level is  {self.score}", align='Center', font=("Arial", 20, 'normal'))

    def game_over(self):
        self.hideturtle()
        self.up()
        self.goto(0, 0)
        self.write('GAME OVER', align='Center', font=('Arial', 30, 'normal'))

    def incr_score(self):
        self.score += 1
        self.clear()
        self.create_table()




