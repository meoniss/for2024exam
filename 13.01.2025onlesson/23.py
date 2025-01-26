def f(cur, fin):
    if cur > fin:
        return 0
    if cur == fin:
        return 1
    if cur < fin:
        return f(cur + 1, fin) + f(cur * 2, fin)
print(f(2, 11) * f(13, 24) + f(2, 10) * f(12, 24))

#ответ: 21