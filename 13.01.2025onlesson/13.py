from itertools import product

countt = 0
for i in product('01', repeat=11):
    if (i.count('1') + 8) % 5 != 0:
        countt += 1
print(countt)