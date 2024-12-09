print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x and (not y)) <= ((not z) or (not w))) and ((w <= x) or y)
                if f == 0:
                    print(x, y, w, z)