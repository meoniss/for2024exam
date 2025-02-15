from itertools import product
countt = 0
for n in product('0123456789ABCDE', repeat=8):
    if n[0] != '0' and n.count('0') == 2 and (n.count('A') + n.count('B') + n.count('C') + n.count('D') + n.count('E') <= 4):
        countt += 1
print(countt)

#что-то очень долго работает 154248381