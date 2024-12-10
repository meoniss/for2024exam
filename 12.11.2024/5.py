maximum = 0
for n in range(123456789, 456789013):
    num = bin(n)[2:]
    num = str(num)
    if n % 2 == 0:
        num = '11' + num
    else:
        num = '1' + num + '10'
    result = int(num, 2)
    maximum = max(maximum, result)
print(maximum)

#ответ: 3974639694