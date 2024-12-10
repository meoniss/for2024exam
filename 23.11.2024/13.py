minsum = 0
sumn = 0
for i in range(1, 1000):
    num = i
    num = '0' + str(num) + '0'
    while '00' not in num:
        num = num.replace('01', '220', 1)
        num = num.replace('02', '1013', 1)
        num = num.replace('03', '113', 1)
    if num.count('1') == 13 and num.count('2') == 18:
        for i in num:
            sumn += int(i)
            minsum = min(minsum, sumn)
print(minsum)