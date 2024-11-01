minn = []
nres = []
result = ''
sum_result = 0
for n in range(1, 1000):
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
    if final_result > 97:
        nres.append(final_result)
        minn.append(n)
print(min(minn))
print(min(nres))

#ответ: 390