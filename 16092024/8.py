lwtters = 'ПАРБОЛ'
count = 0
for n in lwtters:
    for k in lwtters:
        for m in lwtters:
            for p in lwtters:
                for q in lwtters:
                    for t in lwtters:
                        for w in lwtters:
                            for v in lwtters:
                                word = n + k + m + p + q + t + w + v 
                                if word.count('П') == 1 and word.count('А') == 3 and word.count('Р') == 1 and word.count('Б') == 1 and word.count('О') == 1 and word.count('Л') == 1 and word.count('ПР') == 0 and word.count('РП') == 0 and word.count('АА') == 0 and word.count('АО') == 0 and word.count('ОА') == 0 and word.count('БЛ') == 0 and word.count('ЛБ') == 0 and word.count('ПБ') == 0 and word.count('БП') == 0 and word.count('РБ') == 0 and word.count('БР') == 0 and word.count('ЛП') == 0 and word.count('ПЛ') == 0 and word.count('ЛР') == 0 and word.count('РЛ') == 0:
                                    count += 1
print(count)  
#ответ: 192
