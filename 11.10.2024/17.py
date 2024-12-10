number = (49 ** 10) + (7 ** 30) - (49)
new = ''
while number != 0:
    new += str(number % 7)
    number = number // 7
print(new.count('6'))
#ответ: 18