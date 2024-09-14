file = open('C:/Users/Агранович Денис/Documents/GitHub/for2024exam/13092024/for9.txt')
count = 1 #для подсчета количетсва строк
for n in file:
    listt = sorted(list(map(int, n.split()))) #считали числа каждой строки в список
    for i in listt:
        if listt[0] + listt[1] > listt[3] and listt[0] + listt[1] > listt[2]:
            count += 1
print(count)

#ответ: 7369