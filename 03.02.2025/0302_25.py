from fnmatch import *
for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '3?6906*4'):
        print(x)