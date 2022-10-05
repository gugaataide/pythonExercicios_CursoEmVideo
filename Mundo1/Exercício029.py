import random
from time import sleep

print('-=-' * 30)
print('       Vamos jogar! Tente adivinhar o número entre 0 e 5 que eu estou pensando!')
print('-=-' * 30)
user = int(input('Digite um número:'))
pc = random.randint(0, 5)
print ('PROCESSANDO...')
sleep(2)
if pc == user:
    print('Parabéns, você acertou!')
else:
    print('Você errou! o número que eu pensei foi: {}'.format(pc))
