n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite mais um número:'))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor número é: {} \nO maior número é:{}'.format(menor, maior))

#precisei de ajuda para entnder a lógica
