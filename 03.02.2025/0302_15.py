maxA = 0
for A in range(0, 300):
    flag = True
    for y in range(0, 100):
        for x in range(0, 100):
            if ((y + 2*x != 48) or (A < x) or (A < y)) == 0:
                flag = False
    if flag:
        maxA = max(maxA, A)
print(maxA)