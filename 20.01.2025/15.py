for A in range(0, 70):
    flag = True
    for x in range(0, 70):
        for y in range(0, 70):
            if ((x*y < A) or (y > x) or (x >= 8)) == False:
                flag = False
    if flag == True:
        print(A)
        break
