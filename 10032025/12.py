for i in range(0, 2000):
    n = i*'12' + (10-i)*'1'
    while '21' in n:
        n = n.replace('21', '5')
    if n.count('1') + n.count('2')*2 + n.count('5')*5 == 34:
        print(i)