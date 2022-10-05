num = (int(input('Digite o 1° número:')),int(input('Digite o 2° número:')), int(input('Digite o 3° número:')),
       int(input('Digite o 4° número:')))
cont9 = 0
contpar = 0
dvdp2 = 0
for v in num:
       if v == 9:
              cont9 = cont9 + 1
if 3 in num:
       trei = num.index(3) + 1
       print(f'O número 3 foi achado pela primeira vez no {trei}° termo')
print('Os valores pares digitados  foram: ', end=' ')
for dois in num:
       if dois % 2 == 0:
              print(f'{dois}', end=', ')
if cont9 > 0:
       print(f'\nO número 9 apareceu: {cont9} vezes.')