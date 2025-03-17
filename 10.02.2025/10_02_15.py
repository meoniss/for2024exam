f = open('10_02_15.txt')

a = [int(s) for s in f]
# for s in f:
#     a = [int(x) for x in s.split()]
nmax7 = max(a) % 7
nmin5 = min(a) % 5
listt = []
for i in range(len(a) - 2):
    threen = [a[i], a[i+1], a[i+2]]
    len4 = [x for x in threen if len(str(x)) == 4]
    n5 = [x for x in threen if x % 5 == nmin5]
    n7 = [x for x in threen if x % 7 == nmax7]
    if len(n5) <= 1 and len(n7) >= 2 and len(len4) > 0:
        listt.append(sum(threen))
print(len(listt), max(listt))