num = int(input('Digite um número e veja se ele é primo: '))
for c in range(num, 1, -1):
    res = num % c
if res == 0:
    if num == 2:
        print('É PRIMO')
    else:
        print('NÃO É PRIMO')
else:
    print('É PRIMO')