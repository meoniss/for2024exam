for n in range(10000, 3, -1):
    num = '5' + n*'2'
    while '52' in num or '2222' in num or '1122' in num:
        if '52' in num:
            num = num.replace('52', '11', 1)
        if '2222' in num:
            num = num.replace('2222', '5', 1)
        if '1122' in num:
            num = num.replace('1122', '25', 1)    
    if num.count('1')*1 + num.count('2')*2 + num.count('5')*5 == 64:
        print(n)
        break

#ответ: 156    
