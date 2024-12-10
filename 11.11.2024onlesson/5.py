new = ''
for n in range(1, 100000):
    # new += str(n % 2)
    # n = n // 2
    new = bin(n)[2:]
    if int(new) % 5 == 0:
        new = str(int(new, 2)) + '101'
    else:
        new = str(int(new, 2)) + '1'
        if int(new) % 7 == 0:
            new += '111'
        else:
            new += '1'
    if int(new) < 1728404:
        print('new:', new)
        print('n:', n)

# new: 1728311
# n: 17283