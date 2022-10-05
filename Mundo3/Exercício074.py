from random import randint
num = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
maior = -1
menor = 10
for v in num:
    if v > maior:
            maior = v
    elif v < menor:
            menor = v
print('Os números sorteados foram:', num)
print(f' O maior número foi o: {maior}\n' ,f'E o menor foi o: {menor}')