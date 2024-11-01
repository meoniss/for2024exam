final_result = ''
result = ''
for n in range(1, 1000):
    k = n
    while n != 0:
        result += str(n % 2)
        n = n // 2
        break
    if int(k) % 2 == 0:
        result += '10'
    else:
        result += '01'
    result = int(result, 2)
    if result <= 102:
        print(result)

    