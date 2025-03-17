from itertools import product

countt = 0
for i in product('АНДРЕЙ', repeat=6):
    w = ''.join(i)
    if w.count('А') >= 1 and w.count('Й') <= 1:
        countt += 1
print(countt)
