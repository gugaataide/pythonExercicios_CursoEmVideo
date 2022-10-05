n1 = int(input('Digite um número inteiro qualquer:'))
n2 = int(input('Digite outro número inteiro qualquer:'))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('{} e {} são iguais'.format(n1, n2))