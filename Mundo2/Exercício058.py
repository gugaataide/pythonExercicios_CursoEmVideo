import random
print('-=-' * 15)
print('           Jogo da adivinhação!\nTente adivinhar o número que estou pensando!')
print('-=-' * 15)
user = int(input('Digite um número entre 1 e 10: '))
machine = random.randint(1, 10)
cont = 1
while user != machine:
    user = int(input('Você errou! Tente de novo: '))
    cont = cont + 1
print('\033[1;32mVocê ganhou!\033[m Para isso, foram necessárias {} tentativas.'.format(cont))