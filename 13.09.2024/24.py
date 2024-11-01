file1 = open('C:/Users/Агранович Денис/Documents/GitHub/for2024exam/13092024/for24.txt')
file2 = file1.readline()
symbols = '0123456789ABCDEFGHIJ'
maximum = 0
count = 0
for i in range(len(file2)):
    if file2[i] in symbols:
        count += 1
        if count > maximum:
            count = maximum
    else:
        count = 0
print(max(maximum, count))