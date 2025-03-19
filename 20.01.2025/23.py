def f(cur, fin):
    if cur > fin:
        return 0
    if cur == fin:
        return 1
    if cur < fin:
        return f(cur+1, fin) + f(cur*2, fin) + f(cur*3, fin)
print(f(2, 14)*f(14, 28))