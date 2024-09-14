file = open('C:/Users/Агранович Денис/Documents/GitHub/for2024exam/13092024/for17.txt')
count = 0
listofmax = []
listt = [int(i) for i in file]
for i in range(len(listt) - 1):
    if min(listt) % 10 == 5 and (listt[i])**2 + (listt[i+1])**2 < (min(listt))**2:
        count += 1
        listofmax.append((listt[i])**2 + (listt[i+1])**2)
print(count, max(listofmax))

#ответ: 3896 and 99898642