from itertools import product
count = 0
for x in product('012345678', repeat = 5):
    num = ''.join(x)
    if num.count('6') == 1:
        index6 = num.index('6')
        if index6 != len(num) and index6 != 0:
            if int(num[index6 - 1]) % 2 == 0 and int(num[index6 + 1]) % 2 == 0:
                count += 1
        elif index6 == 0:
            if int(num[index6 + 1]) % 2 == 0:
                count += 1
        elif index6 == len(num):
            if int(num[index6 - 1]) % 2 == 0:
                count += 1
print(count)

#idk what's wrong 