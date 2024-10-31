lwtters = ['А', 'К', 'Р', 'У']
res = 0
for n in lwtters:
    for k in lwtters:
        for m in lwtters:
            for p in lwtters:
                for q in lwtters:
                    res += 1
                    if res == 450:
                        print(n, k, m, p, q)
#ответ: КУААК