for n in range(10000, 1, -1):
    num = bin(n)[2:]
    num = str(num)
    sum1 = 0
    for i in num:
        sum1 += int(i)
    mod1 = sum1 % 2
    num = num + str(mod1)
    sum2 = 0
    for i in num:
        sum2 += int(i)
    mod2 = sum2 % 2
    num = num + str(mod2)
    result = int(num, 2)
    if result < 100:
        print(result)
        break
    
#ответ: 96