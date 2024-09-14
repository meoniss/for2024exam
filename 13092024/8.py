lwtters = 'АВОРТ'
count = 0
for n in lwtters:
    for k in lwtters:
        for m in lwtters:
            for p in lwtters:
                count += 1
                if n == 'Т' and k == 'А' and m == 'Р' and p == 'А':
                    print(count)  
#ответ: 516