for x in '0123456789AB':
    for y in '0123456789AB':
        n = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
        if n % 80 == 0:
            print(n // 80)
            break