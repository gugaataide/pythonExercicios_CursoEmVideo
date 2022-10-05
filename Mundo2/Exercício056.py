cont = 0
mv = 0
mulv = 0
nmv = str
for nis in range (1, 6):
    print('-=' * 5, '{}° Pessoa'.format(nis), '-=' * 5)
    n = str(input('Nome = '))
    i = int(input('Idade = '))
    s = str(input('Sexo [M/F] = ')).lower()
    cont = cont + i
    if s == 'm':
      if nis == 1:
          mv = i
      if i > mv:
            mv = i
            nmv = n
    if s == 'f':
        if i < 20.0:
            mulv = mulv + 1
print('A média das idades entre todos do grupo é {} anos.'.format(cont / 5))
print('O homem mais velho é o {} e ele tem {} anos.'.format(nmv, mv))
print ('No grupo, há {} mulheres menores de 20 anos.'.format(mulv))

# precisei de uma ajuda beem pequena.