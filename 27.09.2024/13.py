number = '8'* 99  + '1'
while ('133' in number) or ('881' in number):
    number = str(number)
    if ('133' in number):
        number = number.replace('133', '81', 1)
    else:
        number = number.replace('881', '13', 1)
print(number)

#ответ: 813