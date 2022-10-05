lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
        posme = posma = c
    else:
        if lista[c] > maior:
            maior = lista[c]
            posma = c

        if lista[c] < menor:
            menor = lista[c]
            posme = c
print(f'Você digitou os números: {lista}\nO maior número estava na posição {posma} e foi o: {maior}'
      f'\nE o menor número estava na posição {posme} e foi o: {menor}')