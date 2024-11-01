from turtle import *
size = 20 #чтобы было видно лучше путь, увеличиваем маштаб
left(90) #поворачиваем на ось x
tracer(0) #отслеживание пути
screensize(2000, 2000)
pendown()
right(45)
for i in range(7):
    forward(5 * size)
    right(45)
    forward(10 * size)
    right(135)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size) #сетка
        dot()
done()

#ответ: 27