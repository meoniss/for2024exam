from math import ceil

for i in range(0, 100):
    if (ceil((377*i)/8)*23155)/1024 > 5536:
        print(2**(i-1)+1)
        break
