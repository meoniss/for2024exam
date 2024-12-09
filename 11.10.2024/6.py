num = ''
for n in range(1, 5000):
    num = str(bin(n)[2:])
    num = int(num) // 10
    if n % 2 != 0:
        num = str(num) + '10'
    else:
        num = str(num) + '01'
    result = int(num, 2)
    if result == 2018:
        print(n)

#ответ: 1009