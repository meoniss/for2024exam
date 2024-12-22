def F(cur, end):
    if cur > end:
        return 0
    if cur == end:
        return 1
    if cur < end:
        return F(cur + 1, end) + F(cur + 10, end)
print(F(10, 32))