number = (125) + (25 ** 3) + (5 ** 9)
new = ''
while number != 0:
    new += str(number % 5)
    number = number // 5
print(new.count('0'))
#ответ: 7