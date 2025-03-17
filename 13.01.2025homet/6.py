from turtle import *
tracer(2)
screensize(2000, 2000)
m = 30
left(90)
for i in range(8):
    forward(16*m)
    right(90)
    forward(22*m)
    right(90)
penup()

forward(5*m)
right(90)
forward(5*m)
left(90)
pendown()

for i in range(8):
    forward(52*m)
    right(90)
    forward(77*m)
    right(90)
penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'yellowgreen')
done()