maxn = []
sumnumber = 0
for n in range(0, 10000):
    number = '5' + '2'*n
    while ('52' in number) or ('2222' in number) or ('1122' in number):
        number = str(number)
        if ('52' in number):
            number = number.replace('52', '11', 1)
        if ('2222' in number):
            number = number.replace('2222', '5', 1)
        if ('1122' in number):
            number = number.replace('1122', '25', 1)
    for i in number:
        sumnumber += int(i)
    if sumnumber == 64:
        maxn.append(number)
        break
print(max(maxn))
#ответ: ответа не будет, потому что я переживаю за свой компьютер, ведь ему очень тяжко перебирать 10000 элементов, так еще и сравнивать...TT
#но, ощущение, что программа должна рабтать хорошо! 