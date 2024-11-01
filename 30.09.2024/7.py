from turtle import *
size = 50 #чтобы было видно лучше путь, увеличиваем маштаб
left(90) #поворачиваем на ось x
tracer(0) #отслеживание пути
screensize(2000, 2000)
pendown()
for i in range(3):
    forward(7*size)
    right(90)
forward(8*size)
for i in range(3):
    left(90)
    forward(5*size) 
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * size, y * size) #сетка
        dot()
done()   

#ответ: 43