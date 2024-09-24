for x in range(13):
    n1 = 2 * 13 ** 4 + 6 * 13 ** 3 + x * 13 ** 2 + 9 * 13 + 8
    n2 = 4 * 45 ** 4 + x * 45 ** 3 + 2 * 45 ** 2 + 9 * 45 + 6 
    number = n1 + n2
    if number % 34 == 0:
        print (x, number // 34)

#ответ: 516859