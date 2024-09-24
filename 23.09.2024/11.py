number = '1'*82
while ('11111' in number) or ('888' in number):
    if '11111' in number:
        number = number.replace('11111', '88', 1)
    elif '888' in number: 
        number = number.replace('888', '8', 1)
print(number)

#ответ: 8811