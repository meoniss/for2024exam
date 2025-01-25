print('x y w z | f = 1')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (z == (x <= w)) and (x == (not (w <= y)))
                if f == 1:
                    print(x, y, w, z)
print('________________')
print('x y w z | f = 0')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (z == (x <= w)) and (x == (not (w <= y)))
                if f == 0:
                    print(x, y, w, z)

# ответ: yzwx