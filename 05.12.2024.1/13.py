summ = 0
minn = 0
for n in range(4, 10001):
    num = '5' + n*'2'
    while '52' in num or '1122' in num or '2222' in num:
        if '52' in num:
            num = num.replace('52', '11', 1)
        if '2222' in num:
            num = num.replace('2222', '5', 1)
        if '1122' in num:
            num = num.replace('1122', '25', 1)
        result = num
        if result.count('5')*5 + result.count('1')*1 + result.count('2')*2 == 64:
        # for i in result:
        #     summ += int(i)
        #     if summ == 64:
            print(n)
            print(result)
            break

#ответ: 152