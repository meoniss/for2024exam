f = open('10_02_16.txt')

maxsum = -10000**6
countt = 0
a = [int(x) for x in f]
nmax3 = max(a) % 3
nmin7 = min(a) % 7
for i in range(len(a) - 1):
# n3 = [x for x in a if x % 3 == nmax3]
# n7 = [x for x in a if x % 7 == nmin7]
# if len(n3) >= 1 and len(n7) >= 1:
    if ((a[i] % 3 == nmax3) or (a[i+1] % 3 == nmax3)) and ((a[i] % 7 == nmin7) or (a[i+1] % 7 == nmin7)):
        countt += 1
        maxsum = max(maxsum, sum(a))
print(countt, maxsum)
