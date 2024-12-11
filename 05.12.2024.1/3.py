print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(x <= z)) or (y == w) or y
                if f == 0:
                    print(x, y, w, z)

#ответ: zxyw