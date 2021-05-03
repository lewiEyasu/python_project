from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.setpos(0, -280)
        self.speed('fastest')

    def move_up(self):
        self.fd(25)

    def move_down(self):
        self.backward(25)

    def collision_with_wall(self):
            self.goto(0, -280)
