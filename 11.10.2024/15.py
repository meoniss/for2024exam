from itertools import product
# number ='1'*10 + '2'*3
maxsum = 0
for n in product('12', repeat=13):
    if n.count('1') == 10 and n.count('2') == 3:
        number = ''.join(n)
        while '11' in number:
            if '112' in number:
                number = number.replace('112', '6', 1)
            else:
                number = number.replace('11', '3', 1)
        summ = 0
        for i in (number):
            summ += int(i)
            maxsum = max(maxsum, summ)
print(maxsum)

#ответ: 24