num = 125**5 + 25**9 - 30
s = ''
while num != 0:
    s = str(num % 5) + s
    num //= 5
print(s.count('4'))