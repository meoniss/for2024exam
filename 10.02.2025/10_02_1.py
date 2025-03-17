def F(cur, fin):
    if cur < fin:
        return 0
    if cur ==  fin:
        return 1
    if cur > fin:
        return F(cur - 2, fin) + F(cur // 2, fin)

print(F(38, 16)*F(16, 2))