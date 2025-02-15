f = open('09.csv')

countt = 0
for s in f:
    a = sorted([int(x) for x in s.split(';')])
    listsim = [x for x in a if a.count(x) >= 2]
    if a.count(a[-1]) == 1 and sum(listsim) > a[-1]:
        countt += 1
print(countt)