s = 0
cont = 0
for c in range(0,6):
    n = int(input('digite um número:'))
    if n % 2 == 0:
     cont = cont + 1
     s = s + n
print('Você informou {} valores pares, e a soma deles é: {}'.format(cont, s))