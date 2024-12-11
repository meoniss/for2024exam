from turtle import *
tracer(3)
screensize(2000, 2000)
left(90)
m = 30
for i in range(8):
    right(45)
    forward(6*m)
penup()
for x in range (-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'cyan')
done()

#ответ: 15