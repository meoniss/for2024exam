for n in range(1, 42):
    for m in range(1, 42):
        num = '0' + '1'*n + '2'*m
        while '01' in num or '02' in num:
            num = num.replace('02', '1110', 1)
            num = num.replace('01', '220', 1)
