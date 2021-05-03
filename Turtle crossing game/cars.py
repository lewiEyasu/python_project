from turtle import Turtle
import random
position = [-210, -180, -130, -80, -30, 20, 70, 120, 170, 220, 270]
colors = ['orange', 'red', 'blue', 'green', 'yellow', 'black', 'brown']

class Car(Turtle):

    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_chance = random.randint(1, 4)
        if random_chance == 4:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.goto(300, random.choice(position))
            self.cars.append(new_car)

    def move(self):
        for i in self.cars:
            i.backward(15)
