num = 54*'5' + '7'
while '722' in num or '557' in num:
    if '722' in num:
        num = num.replace('722', '57', 1)
    if '557' in num:
        num = num.replace('557', '72', 1)
print(num)

