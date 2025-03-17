print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = ((not(x) or z) == (y and not(w))) <= (z and y)
                if f == 0:
                    print(x, y, w, z)
