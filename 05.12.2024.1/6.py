count = 0
for n in range(1, 10000):
    num = bin(n)[:2]
    num = num + str(n % 3)
    just5 = int(num, 2) % 5
    num = num + str(just5)
    result = int(num, 2)

    if result >= 1111111110 and result <= 1444444417:
        count += 1
print(count)

######