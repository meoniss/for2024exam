def F(cur, fin):
    if cur > fin:
        return 0
    if cur == fin:
        return 1
    if cur < fin:
        return F(cur + 1, fin) + F(cur + 2, fin) + F(cur + 3, fin)
print(F(1, 7) * F(7, 35))