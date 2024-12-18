from turtle import *
tracer(3)
m = 30
screensize(2000, 2000)
left(90)
for i in range(12):
    right(60)
    forward(1*m)
    right(60)
    forward(1*m)
    right(270)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'orange')
done()

#ответ: 38