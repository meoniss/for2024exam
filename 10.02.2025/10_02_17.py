f = open('10.02.2025/10_02_17.txt')

maxsum = -10000**6
countt = 0
a = [int(x) for x in f]
nmin3 = min(a) % 3
nmax7 = max(a) % 7
for i in range(len(a) - 1):
# n3 = [x for x in a if x % 3 == nmax3]
# n7 = [x for x in a if x % 7 == nmin7]
# if len(n3) >= 1 and len(n7) >= 1:
    if ((a[i] % 3 == nmin3) or (a[i+1] % 3 == nmin3)) and ((a[i] % 7 == nmax7) or (a[i+1] % 7 == nmax7)):
        countt += 1
        maxsum = max(maxsum, (a[i] + a[i+1]))
print(countt, maxsum)