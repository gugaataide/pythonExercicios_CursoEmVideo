n = int(input('Digite um número para calcular seu fatorial:'))
c = n + 1
d = 1
while c > 1:
    c = c - 1
    d = d * c

print('{}! é igual a: {}'.format(n, d))
#precisei de ajuda