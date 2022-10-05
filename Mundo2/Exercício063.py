print('-=-' * 5, 'Sequência de fibonacci', '-=-' * 5)
n = int(input('Quantos temos você quer ver? '))
cont = 0
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while cont < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont = cont + 1
    print('{} -> '.format(t3), end='')
print('Fim')