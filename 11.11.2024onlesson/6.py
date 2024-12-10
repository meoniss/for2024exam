from turtle import *
m = 30
tracer(3)
left(90)
screensize(2100, 2100)
pendown()
for i in range(6):
    forward(6*m)
    right(120)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot('red')
done()