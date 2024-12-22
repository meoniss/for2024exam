def f(a, n):
    if a >= 96 or n > 2:
        return n == 2
    move = [f(a + 1, n + 1)]
    if a % 2 == 0:
        move += [f(a + a//2, n + 1)]
    if a % 3 == 0:
        move += [f(a + a//3, n + 1)]
    if a % 2 != 0 and a % 3 != 0:
        move += [f(2 * a, n + 1)]
    return any (move)
print([amount for amount in range(1, 95 + 1) if f(amount, 0)])