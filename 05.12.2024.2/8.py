from itertools import product
count = 0
for x in product('0234567', repeat = 5):
    num = ''.join(x)
    if (num.count('0') <= 1) and (num.count('2') <= 1) and (num.count('3') <= 1) and (num.count('4') <= 1) and (num.count('5') <= 1) and (num.count('6') <= 1) and (num.count('7') <= 1):
        if (int(num[0]) % 2 != int(num[1]) % 2) and (int(num[1]) % 2 != int(num[2]) % 2) and (int(num[2]) % 2 != int(num[3]) % 2) and (int(num[3]) % 2 != int(num[4]) % 2):
            count += 1
print(count)

#ответ: 216