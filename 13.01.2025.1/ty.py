from turtle import *
from math import *
tracer(3)
screensize(3500, 3500)
m = 20
left(90)
for i in range(9):
    forward(50*m)
    right(90)
    forward(35*m)
    right(90)

penup()
forward(5*m)
right(90)
forward(10*m)
right(90)
pendown()

for i in range(4):
    forward(35*m)
    right(90)
    forward(17*m)
    right(90)
    
penup()
for x in range(-70, 70):
    for y in range(-70, 70):
        goto(x*m, y*m)
        dot(5, 'greenyellow')
done()