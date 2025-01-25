def F(n):
    if n < 10:
        return n
    else:
        return F(n % 10) + F(n // 10)
count = 0
for n in range(1, 2**63):
    if F(n) == 159:
        count += 1
print(count)