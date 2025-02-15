from itertools import product
index = 0
for x in sorted(product('АОУ', repeat=6), reverse=True):
    word = ''.join(x)
    index += 1
    if word == 'ОУУУОО':
        print(index)
