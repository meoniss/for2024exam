import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n-1)
    
print(F(2204) - F(2202))

#ответ: почему-то ничего не печатает