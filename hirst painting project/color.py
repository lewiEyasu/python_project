import random
import colorgram
import turtle

class color:

    color=colorgram.extract('spot.jpg',30)
    rgb=[]

    for i in color:
        rgb.append(i.rgb)



    tim=turtle.Turtle()
    turtle.colormode(255)
    tim.speed('fastest')


    tim.penup()
    tim.setx(-750)
    tim.sety(-400)


    pos_x=-750
    pos_y=-400


    for y in range(0,16):
        for x in range(0,28):
            tim.penup()
            pos_x += 50
            tim.setx(pos_x)
            color=random.choice(rgb)
            tim.dot(16,color)
        pos_y+=50
        pos_x=-750
        tim.sety(pos_y)











    screen=turtle.Screen()
    screen.exitonclick()