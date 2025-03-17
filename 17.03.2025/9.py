f = open('09.csv')

countt = 0
for s in f:
    a = sorted([int(x) for x in s.split(',')])
    average = sum(a)/len(a)
    del2 = [x for x in a if x % 2 == 0]
    nondel2 = [x for x in a if x % 2 != 0]
    #
    hmdel2 = [x for x in del2 if x > average]
    hmnondel2 = [x for x in nondel2 if x > average]
    if hmdel2 > hmnondel2 and sum(del2) < sum(nondel2):
        countt += 1
print(countt)

