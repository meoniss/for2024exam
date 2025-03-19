from turtle import *
tracer(2)
screensize(2000, 2000)
left(90)
m = 30
for i in range(4):
    forward(7*m)
    right(90)
    forward(8*m)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'yellowgreen')
done()
