f = open('20.01.2025/17.txt')
maxx = 0
countt = 0
a = [int(x) for x in f]
for i in range(len(a) - 1):
    if (((a[i] * a[i+1]) % 15 == 0) and ((a[i] + a[i+1]) % 7 == 0)):
        countt += 1
        maxx = max(maxx, (a[i] + a[i+1]))
print(countt, maxx)