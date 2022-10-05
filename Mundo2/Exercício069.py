cont = mdi = fmd20 = h = 0
continuar = str
while True:
    print('-=-' * 12)
    print('       CADASTRE UMA PESSOA.')
    print('-=-' * 12)
    cont = cont + 1
    idade = int(input(f'Qual a idade da {cont}° pessoa?'))
    sexo = str(input(f'Qual o sexo da {cont}° pessoa?[F/M]')).strip().lower()
    if idade >= 18:
        mdi = mdi + 1
    while sexo not in 'mf':
        print('Resposta inválida, por favor tente novamente.')
        sexo = str(input(f'Qual o sexo da {cont}° pessoa?[F/M]')).strip().lower()
        if sexo in 'f':
            if idade < 20:
                fmd20 = fmd20 + 1
        if sexo in 'm':
            h = h + 1
    continuar = str(input('Deseja continuar? [S/N]'))
    while continuar not in 'sn':
        print('resp inv')
        continuar = str(input('Deseja continuar?[S/N]: ')).strip().lower()
    if continuar in 'n':
            break
print(f'Você cadastrou {cont} pessoas\nEntre elas:\n {mdi} Eram maiores de idade\n {h} Eram homens'
      f'\n {fmd20} Eram mulheres com menos de 20 anos')