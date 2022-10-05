n = int(input('Digite um número qualquer:'))
num = n % 2
if  num == 0:
    print('{} é PAR!'.format(n))
else:
    print('{} é IMPAR!'.format(n))