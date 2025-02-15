f = open('0302_24.txt')

s = f.read()
maxx = 0
countB = 0
for i in range(0, len(s)):
    if s[i] == 'B':
        countB += 1
        maxx = max(maxx, countB)
    else:
        countB = 0
print(maxx)