from itertools import product
count = 0
for x in product('012345678', repeat = 11):
    num = ''.join(x)
    if (num.count('0') == 0) and (num.count('1') <= 4) and (num.count('2') <= 4) and (num.count('3') <= 4) and (num.count('4') <= 4) and (num.count('5') <= 4) and num.count('6') <= 4 and num.count('7') <= 4 and num.count('8') <= 4:
        if (int(num[0]) % 2 != int(num[1]) % 2) and (int(num[1]) % 2 != int(num[2]) % 2) and (int(num[2]) % 2 != int(num[3]) % 2) and (int(num[3]) % 2 != int(num[4]) % 2) and (int(num[4]) % 2 != int(num[5]) % 2):
            if (int(num[5]) % 2 != int(num[6]) % 2) and (int(num[6]) % 2 != int(num[7]) % 2) and (int(num[7]) % 2 != int(num[8]) % 2) and (int(num[8]) % 2 != int(num[9]) % 2) and (int(num[9]) % 2 != int(num[10]) % 2):
                count += 1
print(count)

#почему-то ничего не выводит