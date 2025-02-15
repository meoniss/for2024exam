for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        n = int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)
        if n % 56 == 0:
            print(n // 56)
            break