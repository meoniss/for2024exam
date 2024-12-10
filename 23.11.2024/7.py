from turtle import *
tracer(3)
m = 30
screensize(2000, 2000)
left(90)
for i in range(4):
    forward(14*m)
    right(90)
for i in range(5):
    forward(5*m)
    right(45)
penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'blue')
done()
