from itertools import product
count = 0
for x in product('ГЕРАСИМ', repeat = 7):
    num = ''.join(x)
    if (num.count('ЕА') == 0 and num.count('АЕ') == 0 and num.count('АИ') == 0 and num.count('ИА') == 0 and num.count('ЕИ') == 0 and num.count('ИЕ') == 0) and (num.count('ГР') == 0 and num.count('РГ') == 0 and num.count('РС') == 0 and num.count('СР') == 0 and num.count('ГС') == 0 and num.count('СГ') == 0 and num.count('СМ') == 0 and num.count('МС') == 0 and num.count('ГМ') == 0 and num.count('МГ') == 0 and num.count('МР') == 0 and num.count('РМ') == 0) and (num.count('Г') == 1 and num.count('Е') == 1 and num.count('Р') == 1 and num.count('А') == 1 and num.count('С') == 1 and num.count('И') == 1 and num.count('М') == 1):
        count += 1
print(count)

#Ответ: 144