def f (cur, fin):
    if cur < fin or cur == 24:
        return 0
    if cur == fin:
        return 1
    if cur > fin:
        return f(cur - 1, fin) + f(cur - 6, fin) + f(cur // 2, fin)
print(f(34, 29) * f(29, 19) * f(19, 6))