from turtle import *
tracer(2)
screensize(2000, 2000)
left(90)
m = 30
for i in range(2):
    forward(20*m)
    right(90)
    forward(9*m)
    right(90)
penup()
forward(0.5*m)
left(90)
back(9*m)
forward(0.2*m)
pendown()
for i in range(2):
    forward(20*m)
    right(90)
    forward(9*m)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'greenyellow')
done()

#ответ: 8*9 = 72