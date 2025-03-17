for x in '0123456789':
    num = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
    if num % 121 == 0:
        print(num // 121)
