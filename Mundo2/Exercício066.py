cont = som = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont = cont + 1
    som = som + n
m = som / cont
print(f'Você digitou {cont} números.\nA soma entre eles é: {som}\nA média entre eles é {m}')