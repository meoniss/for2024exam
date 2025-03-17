from turtle import *
left(90)
tracer(3)
screensize(2000, 2000)
m = 30
for i in range(9):
    forward(22*m)
    right(90)
    forward(6*m)
    right(90)
penup()
forward(1*m)
right(90)
forward(5*m)
left(90)
pendown()
for i in range(9):
    forward(53*m)
    right(90)
    forward(75*m)
    right(90)
penup()

for x in range(-25, 25):
    for y in range(-25, 25):
        goto(x*m, y*m)
        dot(5, 'khaki4')

done()
