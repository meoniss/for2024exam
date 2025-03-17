print('x y w z')
for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                f = ((not y) <= (z == w)) and ((z <= x) == w)
                if f == 1:
                    print(x, y, w, z)
