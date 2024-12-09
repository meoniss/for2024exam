number = 25 ** 5 + 5 ** 14 - 5
new = ''
while number != 0:
    new += str(number % 5)
    number = number // 5
print(new.count('4'))
#ответ: 9