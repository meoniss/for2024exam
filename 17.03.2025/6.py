from turtle import *
tracer(3)
screensize(2000, 2000)
m = 30
left(90)
for i in range(5):
    forward(9*m)
    right(90)
    forward(3*m)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'pale green')
done()
