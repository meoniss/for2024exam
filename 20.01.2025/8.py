from itertools import product
count = 0
for n in product('0123456', repeat=4):
    if n[0] > n[1] and n[1] > n[2] and n[2] > n[3]:
        count += 1
print(count)
