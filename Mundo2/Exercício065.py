c = cont = som = maior = menor = 0
while c != 'n':
    num = int(input('Digite um número: '))
    som = som + num
    c = str(input('Deseja continuar? [S/N]')).lower().strip()
    cont = cont + 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
m = som / cont
print('Você digitou {} números\nA média entre eles é: {:.2f}\n e o maior número é o {} e o menor foi '
      '{}' .format(cont, m, maior, menor))
