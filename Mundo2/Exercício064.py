n = 0
cont = 0
som = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    som = som + n
    cont = cont + 1

print('Você digitou {} números, e a soma entre eles é {}'.format(cont - 1, som - 999))