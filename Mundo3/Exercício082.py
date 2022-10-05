lista = []
cont = 0
cont5 = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont = cont + 1
    lista.sort(reverse=True)
    if n == 5:
        cont5 = cont5 + 1
    perg = str(input('Deseja continuar?[S/N]')).strip().lower()
    if perg in 'n':
        break
print(f'Você digitou {cont} números, eles foram: {lista}')
if cont5 > 0:
    print(f'O Número 5 foi digitado {cont5} vezes.')
else:
    print('O Número 5 não foi digitado.')
