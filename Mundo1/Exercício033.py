ano = int(input('Escolha um ano qualquer:'))
quatro = ano % 4
cem = ano % 100
qcentos = ano % 400
if quatro == 0 and cem != 0 or qcentos == 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))

#precisei de ajuda na linha 5 (não sabia da função '!=', que quer dizer: diferente)