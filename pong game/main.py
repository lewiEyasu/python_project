from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from score import Score
import time
game_on= True
i = 0
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('black')
line = Turtle()
screen.tracer(0)
line.hideturtle()
line.color('white')
line.rt(90)
line.width(7)
line.penup()
line.goto(0, 280)
player_score = Score(-50)
computer_score = Score(50)

while i < 19:
    line.pendown()
    line.forward(10)
    line.penup()
    line.fd(20)
    i += 1
paddle1 = Paddle((-450, 0))
paddle2 = Paddle((450, 0))
ball = Ball()
screen.update()


screen.listen()

screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle1.down, 'Down')
screen.update()

while game_on:

    screen.update()
    time.sleep(0.01)
    ball.move()
    ball.collision()
    if ball.xcor() > 0:
        paddle2.goto(paddle2.xcor(),ball.ycor())
        #time.sleep(0.01)
    if ball.distance(paddle2) < 50 and (ball.xcor() > 440 or ball.xcor() < -440):
        ball.paddle_collision()
    elif ball.distance(paddle1) < 50 and ball.xcor() < -440:
        ball.paddle_collision()
    elif ball.xcor() == 500 or  ball.xcor() == -500:
        if ball.xcor() == 500:
            player_score.update_scoreboard()
            ball.goto(0, 0)
        elif ball.xcor() == -500:
            computer_score.update_scoreboard()
            ball.goto(0, 0)
    elif player_score.score == 3 or computer_score.score == 3:
        player_score.game_over()
        game_on = False
        break
screen.exitonclick()

