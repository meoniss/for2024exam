print('x y w z')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x or (not y)) and (not(y == z)) and (not w)
                if f == 1:
                    print(x, y, w, z)

#ответ: xzyw