def f(n):
    n = n*2 +(sum(map(int, str(n))) % 2)
    n = n*2 +(sum(map(int, str(n))) % 2)
    n = n*2 +(sum(map(int, str(n))) % 2)
    return n
n1 = 123456789 // 2 // 2 // 2

for i in range(n1 - 100, n1 + 100):
    if f(i) >= 123456789:
        print(i)
        break
n1 = i
n2 = 1987654321 // 2 // 2 // 2
for k in range(n2 - 100, n2 + 100):
    if f(k) > 1987654321:
        print(k)
        break
n2 = k - 1

print(n2 - n1 + 1)

#ответ: 233024691