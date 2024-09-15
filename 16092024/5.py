
nres = []
result = ''
sum_result = 0
for n in range(1, 10000):
    while n != 0:
        result += str(n % 2)
        n = n // 2
        break
    # for i in result:
    #     if i == 1:
    #         sum_result += 1
    #     print(sum_result)
    result += str((result.count('1')) % 2)
    result += str((result.count('1')) % 2)
    
    final_result = int(result, 2)
    if final_result < 100:
        nres.append(final_result)
print(max(nres))

#ответ: 48