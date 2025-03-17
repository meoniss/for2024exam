for r in range(0, 50):
    for m in range(0, 50):
        for y in range(0, 50):
            n = '0' + '1'*r + '2'*m + '3'*y + '0'
            while '00' not in n:
                n = n.replace('01', '210', 1)
                n = n.replace('02', '3101', 1)
                n = n.replace('03', '2012', 1)
            if n.count('1') == 61 and n.count('2') == 50 and n.count('3') == 18:
                print(r + m + y + 2)
