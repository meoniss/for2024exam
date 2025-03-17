from itertools import product

countt = 0
for i in product(sorted('ABCDX'), repeat=4):
    w = ''.join(i)
    if w.count('X') == 1:
        countt += 1
print(countt)
