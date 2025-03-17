f = open('17.txt')
s = [int(i) for i in f]
for n in range(0, len(s) - 2):
    a = sorted([s[n], s[n+1], s[n+2]])
    if abs(s[n]) % 10000 == 321:
    iflen5 = [x for x in a if len(x) == 5]
    ifdel5 = [x for x in a if x % 5 == 0]
