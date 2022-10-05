import random
print('-=-' * 20)
print(' ' * 10, 'Vamos jogar pedra, papel ou tesoura?')
print('-=-' * 20)
itens = ['Pedra', 'Papel', 'Tesoura']
player = int(input(' [0] Pedra \n [1] Papel \n [2] Tesoura \nEscolha um:'))
machine = random.randint(0,2)
print('Você escolheu:{}'.format(itens[player]))
print('Eu escolhi:{}'.format(itens[machine]))
if player == 0:
    if machine == 0:
        print('\033[1;33mEmpate!\033[m')
    elif machine == 1:
        print('\033[1;31mVocê perdeu!\033[m Papel vence a pedra.')
    elif machine == 2:
        print('\033[1;32mVocê ganhou!\033[m Pedra vence a tesoura.')
elif player == 1:
    if machine == 0:
        print('\033[1;32mVocê ganhou!\033[m Papel vence a pedra.')
    elif machine == 1:
        print('\033[1;33mEmpate!\033[m')
    elif machine == 2:
        print('\033[1;31mVocê perdeu!\033[m Tesoura vence o papel.')
elif player == 2:
    if machine == 0:
        print('\033[1;31mVocê perdeu!\033[m Pedra vence a tesoura.')
    elif machine == 1:
        print('\033[1;32mVocê ganhou!\033[m Tesoura vence o papel.')
    elif machine == 2:
        print('\033[1;33mEmpate!\033[m')
