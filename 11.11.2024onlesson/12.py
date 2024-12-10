n = 125*'8'
while ('333' in n) or ('888' in n):
    if ('333' in n):
        n = n.replace('333', '8', 1)
    else:
        n = n.replace('888', '3', 1)
print(n)
