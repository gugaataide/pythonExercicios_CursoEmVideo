print('-=-' * 12)
print(' ' * 5, 'ANALISADOR DE TRIÂNGULOS')
print('-=-' * 12)
l1 = float(input('Digite um segmento:'))
l2 = float(input('Digite outro segmento:'))
l3 = float(input('Digie mais um segmento:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses segmentos FORMAM um triângulo!')
else:
    print('Esses segmentos NÃO FORMAM um triângulo!')

# precisei de ajuda para escrever a lei de existência de um triângulo
