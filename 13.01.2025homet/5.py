def f(N):
    s = ''
    while N > 0:
        s = str(N % 3) + s
        N //= 3
    return s
    
for n in range(1, 10000):
    num = f(n)
    if n % 3 == 0:
        num = num + num[-2:]
    else:
        summ = num.count('1') + num.count('2')*2
        num = num + f(summ)
    result = int(num, 3)
    if result > 220 and result % 2 == 0:
        print(result)
        break
