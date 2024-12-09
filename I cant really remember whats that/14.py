results = []
for x in range(11):
    for y in range(11):
        n1 = (x * 11 ** 4) + (3 * 11 ** 3) + (4 * 11 ** 2) + (1 * 11) + (y)
    for x in range(19):
        for y in range(19):
            n2 = (5 * 11 ** 4) + (6 * 11 ** 3) + (x * 11 ** 2) + (1 * 11) + (y)
            twn = n1 + n2 #the whooooole number.
            if twn % 305 == 0:
                results.append(twn)
print(min(results) // 305)

#ответ: 281