from turtle import *
size = 50 #чтобы было видно лучше путь, увеличиваем маштаб
left(90) #поворачиваем на ось x
tracer(0) #отслеживание пути
screensize(2000, 2000)
pendown()
for i in range(12):
    right(60)
    forward(1 * size)
    right(60)
    forward(1 * size)
    right(270)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size) #сетка
        dot()
done()

#ответ: 38