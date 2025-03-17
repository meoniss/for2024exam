def f(x, A):
    return ((120 % A == 0) and ((not(x % А == 0)) <= ((x % 18 == 0) <= (not((x % 24 == 0))))))
for A in range(1, 2000):
    for x in range(1, 2000):
        if f(x, A) == 1:
            print(A)
