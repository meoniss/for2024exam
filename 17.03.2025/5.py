for n in range(100, 1000):
    n = str(n)
    sum12 = int(n[0]) + int(n[1])
    sum23 = int(n[1]) + int(n[2])
    new = str(max(sum12, sum23)) + str(min(sum12, sum23))
    if new == '159':
        print(n)
