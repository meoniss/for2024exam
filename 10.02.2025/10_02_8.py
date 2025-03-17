def f(n):
    deli = set()
    for i in range(2, n):
        if n % i == 0:
            deli.add(i)
            deli.add(n // i)
        n //= i
    alld = sorted(deli)
    if len(alld) < 2:
        return 0
for N in range(110_250_000, 110_300_000 + 1):
    if N % 10000 == 1002:
        print(N)
