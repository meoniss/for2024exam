for n in range(1000, 10001):
    strn = str(n)
    sum12 = int(strn[0]) + int(strn[1])
    sum23 = int(strn[1]) + int(strn[2])
    sum34 = int(strn[2]) + int(strn[3])
    first_part = str(max(sum12, sum23, sum34 - max(sum12, sum23, sum34)))
    second_part = str(max(sum12, sum23, sum34))
    result = first_part + second_part
    if result == '1315':
        print(n)
#ответ: 9496