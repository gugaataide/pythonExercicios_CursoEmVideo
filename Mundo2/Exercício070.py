print('-' * 15)
print(' Lojas Taraide')
print('-' * 15)
contador = soma = maidimil = 0
while True:
    prod = str(input('Nome do produto: '))
    price = float(input(f'Preço do(a) {prod}: R$ '))
    contador = contador + 1
    soma = soma + price
    if contador == 1:
        menor = price
        ndm = prod
    else:
        if price < menor:
            menor = price
            ndm = prod
    if price > 1000.00:
        maidimil = maidimil + 1
    contin = ' '
    while contin not in 'sn':
        contin = str(input('Deseja continuar adicionando ítens? [S/N] ')).strip().lower()
    if contin in 'n':
        break
print(f' Total da compra: \033[1;32mR${soma}\033[m\n '
      f'\033[1;33m{maidimil}\033[m produtos custam mais de R$1000.00 '
      f'\n O produto mais barato foi o(a): \033[1;32m{ndm}\033[m')