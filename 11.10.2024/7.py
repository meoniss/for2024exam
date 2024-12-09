from turtle import *
screensize(2000, 2000)
tracer(3)
m = 30
left(90)
for i in range(4):
    forward(8 * m)
    right(90)
for i in range(3):
    forward(12 * m)
    right(120)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(5, 'blue')
done()

#ответ: 57
