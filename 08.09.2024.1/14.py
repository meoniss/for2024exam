#yx3207 + 1x3y39.
for x in '0123456':
    for y in '0123456':
        n = int(y + x + '3' + '2' + '0', 7) + int('1' + x + '3' + y + '3', 9)
        if n % 181 == 0:
            print(n // 181)
            break

#ответ: 148