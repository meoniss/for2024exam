from fnmatch import *
for x in range(0, 10**8, 2622):
    if fnmatch(str(x), '1?4*6?8'):
        print(x, x // 2622)