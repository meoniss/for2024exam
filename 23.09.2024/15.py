for x in range(12):
    n1 = 2 * 18 ** 3 + 8 * 18 ** 2 + x * 18  + 2 
    n2 = 9 * 12 ** 3 + 3 * 12 ** 2 + x * 12 + 5
    number = n1 + n2
    if number % 133 == 0:
        print (x, number // 133)

#ответ: 229