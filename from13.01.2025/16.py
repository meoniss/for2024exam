from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 5:
        return n
    else:
        return(2*n) * f(n - 4)

for i in range(1, 400000000000000000):
    f(i)

print((f(13766) - 9) * (f(13762) // f(13758)))