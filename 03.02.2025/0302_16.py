from functools import lru_cache

@lru_cache()
def f(n):
    if n < 9:
        return n
    else:
        return f(n % 9) + f(n // 9)
countt = 0

for n in range(4*6**20, 5*6**20+1):
    if f(n) == 121:
        countt += 1
print(countt)