from itertools import product
count = 0
for x in product('ABCDXYZ', repeat = 4):
    num = ''.join(x)
    if (num.count('X') == 1 or num.count('Y') == 1 or num.count('Z') == 1) and (num[0] == 'X' or num[0] == 'Y' or num[0] == 'Z'):
        count += 1
print(count)

#ответ: 828