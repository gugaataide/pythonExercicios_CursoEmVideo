f = str(input('Digite uma frase: ')).lower().strip()
palavras = f.split()
join = ''.join(palavras)
inverso = ''
for c in range(len(join) - 1, -1, -1):
    inverso = inverso + join[c]
if inverso == join:
    print('O inverso de {} é {}'.format(join, inverso))
    print('portanto, a frase É PALÍNDROMA')
else:
    print('O inverso de {} é {}'.format(join, inverso))
    print('portanto,a frase NÃO É PALÍNDROMA')