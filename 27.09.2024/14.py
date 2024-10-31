number = 125 + 25 ** 3 + 5 ** 9
zero = 0
while number:
    if number % 5 == 0:
        zero += 1
    number = number // 5
print(zero)
#ответ: 7