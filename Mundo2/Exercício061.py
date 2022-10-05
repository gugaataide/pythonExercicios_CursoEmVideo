num = int(input('Qual é o primeiro termo da P.A? '))
rz = int(input('Qual a razão da P.A? '))
print('O 1° termo da P.A é: \033[1;32m{}\033[m'.format(num))
termo = 1
while termo < 10:
    num = num + rz
    termo = termo + 1
    print('O {}° termo da P.A é: \033[1;32m{}\033[m'.format(termo, num))
