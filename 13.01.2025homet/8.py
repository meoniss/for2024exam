from itertools import product

index = 0
for i in product(sorted('ЯНВАРЬ'), repeat=5):
    w = ''.join(i)
    index += 1
    if w[0] != 'Я' and w.count('Ь') <= 1 \
    and w.count('ЯЯ') == 0 and w.count("ЯЯЯ") == 0 \
    and w.count("ЯЯЯЯ") == 0:
        print(index, w)    