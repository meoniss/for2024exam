sumn = 0
def F(n):
    if n < 15:
        return n
    else:
        return F(n % 15)*F(n // 15)
    
for i in range(30**4):
    if F(i) == 7560:
        sumn += 1
print(sumn)

#ответ: 1832
