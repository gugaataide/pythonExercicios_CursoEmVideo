num = float(input('Digite o primeiro termo da P.A: '))
rz = float(input('Digite a razão da P.A: '))
cont = 1
print('1° termo = {}'.format(num))
for c in range(1,10):
    num = num + rz
    cont = cont + 1
    print('{}° termo: {}'.format(cont, num))