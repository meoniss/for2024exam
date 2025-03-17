from fnmatch import *
for x in range(0, 10**10, 18579):
    if fnmatch(str(x), '54?1?3*7'):
        print(x, x//18579)