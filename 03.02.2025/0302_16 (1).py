from functools import *

@lru_cache(None)
def f(n):
    if n < 9:
        return n
    else:
        return f(n % 9) + f(n // 9)
for i in range(100**13):
    f(i)
countt = 0
for n in range(4*6**20, 5*6**20):
    if f(n) == 121:
        countt == 1
print(countt)