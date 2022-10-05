r = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while r != 5:
    print('-=-=-=-\033[1;35mO que você deseja fazer com esses números?\033[m-=-=-=-')
    r = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Digitar outros números\n[5] Sair\n Resposta: '))
    if r == 1:
        print('A soma de {} e {} é: {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('{} é o maior número.'.format(n1))
        elif n2 > n1:
            print('{} é o maior número.'.format(n2))
        else:
            print('{} e {} são iguais.'.format(n1, n2))
    elif r == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
print('Finalizando...')