f = open('9.txt')

countt = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    lsim = [x for x in a if a.count(x) == 2]
    ldif = [x for x in a if a.count(x) == 1]
    if len(lsim) == 2 and len(ldif) == 4:
        if sum(ldif)/len(ldif) <= sum(lsim):
            countt += 1

print(countt)
