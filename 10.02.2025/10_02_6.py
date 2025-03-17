f = open('10_02_6.txt')
s = f.readline()
alphabett = '0123456789ABCDEFGHIJKLMNOP'
countt = 0
maxx = 0
for i in range(len(s)):
    if s[i] in alphabett:
        countt += 1
        if countt > maxx:
            maxx = countt
    else:
        countt = 0
print(maxx)