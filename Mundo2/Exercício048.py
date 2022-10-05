s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('A soma de todos os {} números ímpares múltiplos de 3 no intervalo de 1 -> 500 é \033[1;32m{}\033[m'.format(cont, s))