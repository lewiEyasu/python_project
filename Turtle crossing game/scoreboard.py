from turtle import Turtle


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.write(f'Level:{self.level}', align='center', font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f'Level:{self.level}', align='center', font=("Arial", 15, "normal"))