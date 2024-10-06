maxn = []
sumnumber = 0
for n in range(69, 1000):
    number = '0' + '1'*n + '2'*n + '0'
    while ('00' in number):
        number = str(number)
        number = number.replace('02', '101', 1)
        number = number.replace('11', '2', 1)
        number = number.replace('12', '21', 1)
        number = number.replace('010', '00', 1)
    for i in number:
        sumnumber += int(i)
    if (sumnumber % 2 != 0) and (sumnumber % 3 != 0) and (sumnumber % 5 != 0):
        print(sumnumber, n)

#ответ: без понятия сколько