maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa?'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {}\nE o menor peso foi {}'.format(maior , menor))

# precisei ver a resolução