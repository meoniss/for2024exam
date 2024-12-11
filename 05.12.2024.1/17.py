import sys
sys.setrecursionlimit(3000000)

def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n-1)
    
print(F(2024) - F(2022))

#не печатает почему-то