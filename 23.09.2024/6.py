for n in range(100, 1001):
    strn = str(n)
    sum12 = int(strn[0]) + int(strn[1])
    sum23 = int(strn[1]) + int(strn[2])
    result = str(min(sum12, sum23)) + str(max(sum12, sum23))
    if result == '714':
        print(n)
        break

#ответ: 168