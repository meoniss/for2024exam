f = open('13.01.2025homet\9.txt')

index = 0
for s in f:
    a = [int(x) for x in s.split()]
    index += 1
    lsim = [x for x in a if a.count(x) == 3]
    ldif = [x for x in a if a.count(x) == 1]
    if len(lsim) == 6 and len(ldif) \
    and sum(lsim)/6 < max(ldif):
        print(index, a)
