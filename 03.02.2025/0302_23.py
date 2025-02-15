def f(cur, fin):
    if cur > fin:
        return 0
    if cur == fin:
        return 1
    if cur < fin:
        return f(cur + 2, fin) + f(cur + 5, fin)
print(f(1, 20))