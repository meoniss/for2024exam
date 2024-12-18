#ПАРАБОЛА
count = 0
s1 = 'ПРБЛ'
s2 = 'АО'
from itertools import product
for i in product('ПАРБОЛ', repeat=8):
    word = ''.join(i)
    if word.count('П') == 1 and word.count('А') == 3 and word.count('Р') == 1 and word.count('Б') == 1 and word.count('Л') == 1 and word.count('О') == 1:
        if word.count('АО') == 0 and word.count('ОА') == 0 and word.count('ПБ') == 0 and word.count('БП') == 0:
            if word.count('ПР') == 0 and word.count('РП') == 0 and word.count('РБ') == 0 and word.count('БР') == 0:
                if word.count('БЛ') == 0 and word.count('ЛБ') == 0 and word.count('ЛП') == 0 and word.count('ПЛ') == 0:
                    if word.count('ЛР') == 0 and word.count('РЛ') == 0:
                        count += 1
print(count)

#ответ: 336
