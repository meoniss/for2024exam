for x in('012345678'):
    M = int(f'842{x}5', 9) 
    N = int(f'8{x}725', 9)
    
    for A in range(0, 2000):
        if (M + A) % N == 0:
            print(A)
            break