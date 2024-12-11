from turtle import *
tracer(3)
screensize(2000, 2000)
m = 30
left(90)
for i in range(4):
    forward(12*m)
    right(90)
for i in range(5):
    forward(4*30)
    right(45)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'pink')
done()

#ответ: 50