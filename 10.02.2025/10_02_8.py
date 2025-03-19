from sys import *
setrecursionlimit(30000000)
def f(n):
    deli = set()
    for i in range(n//2, n):
        if n % i == 0:
            deli.add(i)
            deli.add(n // i)
            n = n // i
    return sorted(deli)
for N in range(110_250_000, 110_300_000 + 1):
    delit = f(N)
    if len(delit) >= 2:
        M = delit[-1] + delit[-2]
        if M % 10000 == 1002:
            print(N)
