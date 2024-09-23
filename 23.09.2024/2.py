print('f s t') #для удобства
for f in range(2): #так как принимает значения 0 или 1
    for s in range(2):
        for t in range(2):
            function = ((f or s) <= (s == t))
            if function == 0:
                print(f, s, t)

# ответ на эту задачу: fst where f = first s = second t = third => x y z

# f s t
# 1 1 0
# 0 0 1
# 0 1 1 