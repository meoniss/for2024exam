print('x y w z') #для удобства
for x in range(2): #так как принимает значения 0 или 1
    for y in range(2):
        for w in range(2):
            for z in range(2):
                function = (((x and (not y)) or (x == z)) or (not w))
                if function == 0:
                    print(x, y, w, z)

# ответ на эту задачу: wzyx