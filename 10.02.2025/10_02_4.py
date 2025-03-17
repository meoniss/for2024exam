f = open('10_02_4.txt')

for s in f:
    s = s.replace('**', '* *')
    s = s.replace('--', '- -')
    s = s.replace('*-', '* -')
    s = s.replace('-*', '- *')
    s = s.replace('*0', '*')
    s = s.replace('-0', '-')