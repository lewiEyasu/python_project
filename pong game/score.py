from turtle import Turtle


class Score(Turtle):

    def __init__(self,x_position):

        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x_position, 250)
        self.write(f'{self.score}', align='center', font=("Arial", 30, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=("Arial", 30, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', align='center', font=("Arial", 30, "normal"))