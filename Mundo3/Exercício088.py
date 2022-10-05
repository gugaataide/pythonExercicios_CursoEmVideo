lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som = []
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um número para [{l},{c}]'))
        som.append(lista[l][c])
