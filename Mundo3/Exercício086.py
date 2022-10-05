lista = [[],[]]
for c in range(0,7):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os números pares foram: {sorted(lista[0])}\nE os ímpares foram: {sorted(lista[1])}')
