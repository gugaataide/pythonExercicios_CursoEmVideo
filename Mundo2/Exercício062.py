num = int(input('Qual é o primeiro termo da P.A? '))
rz = int(input('Qual a razão da P.A? '))
print('O 1° termo da P.A é: \033[1;32m{}\033[m'.format(num))
termo = 1
plus = 10
lim = 0
while plus != 0:
    lim = lim + plus
    while termo < lim:
        num = num + rz
        termo = termo + 1
        print('O {}° termo da P.A é: \033[1;32m{}\033[m'.format(termo, num))
    plus = int(input('Quantos termos a mais você deseja calcular?'))

