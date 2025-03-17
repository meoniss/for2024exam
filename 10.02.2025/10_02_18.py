from sys import *
setrecursionlimit(200000)
def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return 2 * n + F(n - 1)
print(F(2024) - F(2022))