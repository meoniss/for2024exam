number = '7'*85
while ('333' in number) or ('777' in number):
    if '333' in number:
        number = number.replace('333', '7', 1)
    else: 
        number = number.replace('777', '3', 1)
print(number)

#ответ: 377