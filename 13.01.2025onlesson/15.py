countt = 0
for A in range(0, 300):
    flag = True
    for y in range(0, 100):
        for x in range(0, 100):
            if (((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))) == 0:
                flag = False
    if flag:
        countt += 1
print(countt)