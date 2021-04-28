from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 5
        self.y_move = 10
        self.speed('fastest')

    def collision(self):
        if self.ycor() == 300 or self.ycor() == -300:
            self.y_move *= -1




    def paddle_collision(self):

       # if self.xcor() == 500 or self.xcor() == -500:
        self.x_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


