number = '1'*78
while ('111' in number):
    number = number.replace('111', '2', 1)
    number = number.replace('222', '11', 1)
print(number)

#ответ: 377