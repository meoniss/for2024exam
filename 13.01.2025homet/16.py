from functools import *
@lru_cache(None)
def F(n):
    if n < 5:
        return n
    else:
        return 2*n * F(n - 4)

for i in range(5, 14000):
    F(i)

print(((F(13766) - 9*F(13762)))/F(13758))