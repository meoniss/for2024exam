countn = 0
def f(n):
    if n < 10:
        return n
    else:
        return f(n % 10) + f(n // 10)
    
for n in range(1, 2**63):
    if f(n) == 159:
        countn += 1
print(countn)

#ответ: очень долгое время приходится выполнять(