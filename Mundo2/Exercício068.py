import random
print('-=-' * 15)
print('         Vamos jogar par ou ímpar?')
print('-=-'* 15)
cont = -1
while True:
    nuser = int(input('Digite um número:'))
    pi = str(input('Par ou Impar?')).strip().lower()
    machine = random.randint(1, 10)
    juntos = nuser + machine
    cont = cont + 1
    if juntos % 2 == 0:
        if pi == 'par':
            print('Você ganhou! Vamos denovo!')
        else:
            print(f'Você perdeu, mas antes ganhou {cont} vezes!')
            break
    else:
        if pi == 'impar':
            print('Você ganhou! Vamos denovo!')
        else:
            print(f'Você perdeu, mas antes ganhou {cont} vezes!')
            break