from turtle import *
size = 50 #чтобы было видно лучше путь, увеличиваем маcштаб
left(90) #поворачиваем на ось x
tracer(0) #отслеживание пути
screensize(2000, 2000)
pendown()
for i in range(6):
    forward(10 * size)
    right(60)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size) #сетка
        dot()
done()

#ответ: 268
