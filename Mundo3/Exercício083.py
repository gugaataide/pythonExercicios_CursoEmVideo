lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    continuar = str(input('Deseja continuar adicionando números?[S/N]: '))
    if continuar in 'Nn':
        break
print(f'Você digitou os números: {lista}\n'
      f'entre eles {listap} eram números pares\n'
      f'E {listai} eram números ímpares')