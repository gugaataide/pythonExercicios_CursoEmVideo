cont = 0
galera = []
listapesoleve = []
listanomeleve = []
listapesopesado = []
listanomepesado = []
leve = 999
pesado = 0
while True:
    cont += 1
    pessoa = [[str(input(f'Qual o nome da {cont}° pessoa?'))], int(input(f'Qual o peso da {cont}° pessoa [KG]?'))]
    galera.append(pessoa[:])

    if pessoa[1] >= pesado:
        if pessoa[1] > pesado:
            listanomepesado.clear()
        listapesopesado.clear()
        pesado = pessoa[1]
        listanomepesado.append(pessoa[0])
        listapesopesado.append(pessoa[1])
    elif pessoa[1] <= leve:
        if pessoa[1] < leve:
            listanomeleve.clear()
        listapesoleve.clear()
        leve = pessoa[1]
        listanomeleve.append(pessoa[0])
        listapesoleve.append(pessoa[1])
    perg = str(input('Deseja continuar?[S/N]: ')).strip().lower()
    if perg in 'n':
        break
print(f'Foram cadastradas {cont} pessoas.\n A(s) pessoa(s) mais leve(s) é(são): {listanomeleve} que pesa(m) {listapesoleve}kg'
      f'\n A(s) pessoa(s) mais pessada(s) é(são): {listanomepesado} que pesa(m) {listapesopesado}[KG]')