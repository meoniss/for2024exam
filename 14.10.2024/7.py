from itertools import product
count = 0
for x in product('0123456789', repeat = 5):
    num = ''.join(x)
    if int(num[0]) > int(num[1]) and int(num[1]) > int(num[2]) and int(num[2]) > int(num[3]) and int(num[3]) > int(num[4]):
        count += 1
print(count)

#ответ: 252