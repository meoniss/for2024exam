for n in range(0, 100):
    for m in range(0, 100):
        for k in range(1, 100):
            number = '0' + '1'*n + '2'*m + '3'*k
            while ('01' in number) or ('02' in number) or ('03' in number):
                number = str(number)
                number = number.replace('01', '2302', 1)
                number = number.replace('02', '10', 1)
                number = number.replace('03', '201', 1)
            if number.count('1') == 40 and number.count('2') == 10 and number.count('3') == 8:
                print(n)
                break

#ответ: 6