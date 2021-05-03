from turtle import Screen
from player import Player
from cars import Car
import time
from scoreboard import Score


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
level = Score()
car = Car()


screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

speed = 0.1
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()

    car.create_cars()
    car.move()

    if player.ycor() >= 280:
        player.collision_with_wall()
        level.update_scoreboard()
        speed -= 0.02
    for i in car.cars:
        if i.xcor() < 100 and i.distance(player) < 20:
            level.game_over()
            game_on = False

screen.exitonclick()
