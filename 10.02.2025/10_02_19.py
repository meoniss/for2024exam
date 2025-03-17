def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return F((4*n - F(n-3))//8)
    if n > 2 and n % 2 != 0:
        return F((4*n - F(n-1)+ F(n-2))//8)
print(F(52) - F(38))