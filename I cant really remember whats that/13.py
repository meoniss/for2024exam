for n in range(1, 1000):
    number_first = '0' + n + '0'
    number_last = '1'*13 + '2'*18
    while ('00' in number_first):
        number_first = str(number_first)
        number_first = number_first.replace('01', '220', 1)
        number_first = number_first.replace('02', '1013', 1)
        number_first = number_first.replace('03', '1120013', 1)
    if number_first == number_last:
        print(n + 2)

#ответ: не знаю D: