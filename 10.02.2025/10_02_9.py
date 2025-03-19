from sys import *
setrecursionlimit(30000000)
def f(n):
    deli = set()
    for i in range(1, n+1):
        k = n
        if k % i == 0:
            deli.add(i)
            deli.add(k // i)
            k = k // i
    return deli
maxdeli = 0
maxn = 0
for N in range(568_023, 569_230 + 1):
    lendeli = len(f(N))
    if lendeli > maxdeli:
        maxdeli = lendeli
        maxn = N

print(maxdeli, maxn)
