# minx = 0
# miny = 0
minresult = []
for x in range(0, 12):
    for y in range(0, 12):
        num1 = y*12**0 + 1*12**1 + 3*12**2 + 2*12**3 + x*12**4
        num2 = y*14**0 + 8*14**1 + 9*14**2 + x*14**3 + 8*14**4 + 7*14**5
        if (num1 + num2) % 99 == 0:
            result = (num1 + num2)//99
            minresult.append(result)
print(x, y, min(minresult))

#ответ: 41428
