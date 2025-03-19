f = open('9_02.txt')
count = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[0] + a[1] <= a[2] or a[0] + a[1] <= a[3] or a[1] + a[2] <= a[3]:
        count += 1
print(count)