lista = []
cont = 0
while True:
    l = int(input('Digite um número: '))
    if l not in lista:
        lista.append(l)
    else:
        print('Este número já está na lista. Tente outro.')
    continuar = str(input('Deseja continuar? [S/N]')).lower().strip()
    if continuar in 'n':
        break
print(f'Você digitou os números {sorted(lista)}')