for n in range(100, 1000):
    n = str(n)
    sum12 = int(n[0]) + int(n[1])
    sum23 = int(n[1]) + int(n[2])
    num = str(min(sum12, sum23)) + str(max(sum12, sum23))
    if num == '714':
        print(n)
        
