for x in '0123456789ABCDEFGHIJKLMNO':
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if num % 24 == 0:
        print(x, num // 24)