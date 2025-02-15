countt = 0
s = '0' + 12*'1' + 15*'2' + '17'*3
while '01' in s or '02' in s or '03' in s:
    if '01' in s:
        s = s.replace('01', '103', 1)
    if '02' in s:
        s = s.replace('01', '10', 1)
    if '03' in s:
        s = s.replace('03', '210', 1)
    countt = s.count('2')
print(countt)
