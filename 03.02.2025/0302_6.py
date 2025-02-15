from turtle import *
tracer(2)
screensize(2000, 2000)
m = 30
left(90)
for i in range(4):
    forward(6*m)
    right(150)
    forward(6*m)
    right(30)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'MediumTurquoise')
done()