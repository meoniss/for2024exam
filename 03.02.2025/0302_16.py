from functools import lru_cache

@lru_cache()
def f(n):
    if n < 9:
        return n
    else:
        return f(n % 9) + f(n // 9)

print(f(5*6**20, 9) - f(4*6**20-1, 9))