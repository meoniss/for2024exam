maxx = 0
for n in range(100, 1, -1):
    num = bin(n)[2:]
    num = num[::-1]
    if num[0] == '0':
        num = num[1:]
    res = int(num, 2)
    if res == 13:
        print(n)
        break

