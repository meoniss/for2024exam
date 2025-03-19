f = open('9.txt')

count = 0
for s in f:
    a = [int(x) for x in s.split()]
    listsim = [x for x in a if a.count(x) == 2]
    listdif = [x for x in a if a.count(x) == 1]
    if len(listsim) == 4 and len(listdif) == 3 and sum(listdif)//3 < sum(listsim)//4:
        count += 1
print(count)