for A in range(0, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if (((x - 3*y) < A) or (y > 400) or (x > 56)) == 0:
                flag = False
    if flag:
        print(A)
        break