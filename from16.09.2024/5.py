count = 0
for n in range(1000, 10001):
    strn = str(n)
    sum12 = int(strn[0]) + int(strn[1])
    sum34 = int(strn[2]) + int(strn[3])
    result = str(min(sum12, sum34)) + str(max(sum12, sum34))
    if result == '616':
        count += 1
print(count)
#ответ: 39