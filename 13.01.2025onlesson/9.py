f = open('for9.txt')

countt = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if not(a[0] + a[1] >= a[2] and a[0] + a[1] >= a[3] and a[0] + a[2] >= a[3] and a[1] + a[2] >= a[3]):
        countt += 1
print(countt)