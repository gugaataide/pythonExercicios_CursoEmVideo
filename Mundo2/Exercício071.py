print('=' * 20)
print(' Banco do Guguinha')
print('=' * 20)
saque = int(input('Quanto você quer sacar? R$'))
montante = saque
cedula = 50
contced = 0
while True:
    if montante >= cedula:
        montante = montante - cedula
        contced = contced + 1
    else:
        if contced > 0:
            print(f'Você irá sacar {contced} cédulas de  R${cedula}')
        contced = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        if montante == 0:
            break
