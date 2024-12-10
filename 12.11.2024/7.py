from turtle import *
screensize(3000, 3000)
m = 20
tracer(3)
left(90)
pendown()
for i in range(2):
    forward(24*m)
    right(90)
    forward(10*m)
    right(90)

forward(3*m)
left(90)
forward(13*m)
right(90)

for i in range(2):
    forward(9*m)
    right(90)
    forward(32*m)
    right(90)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'blue')
done()

#117 90 120 81 30 => ответ: 120