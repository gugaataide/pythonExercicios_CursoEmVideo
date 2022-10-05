t = 0
n = int(input('Digte um número:'))
for c in range(1, 11):
    tab = t + c
    res = n * tab
    print('{} X {} = {}'.format(n, c, res))