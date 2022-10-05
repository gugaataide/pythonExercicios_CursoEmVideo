num = int(input('Digite um número inteiro qualquer:'))
opc = int(input('Você deseja converter esse número para: \n [1] BINÁRIO \n [2] OCTAL \n [3] HEXADECIMAL \n Resposta:'))
if opc == 1:
    print('{} convertido para binário é: {} !'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para octal é: {} !'.format(num, oct(num)[2:]))
elif opc == 3:
    print ('{} convertido para hexadecimal é: {} !'.format(num, hex(num)[2:]))
else:
    print('\033[1;31m ERRO! você não digitou uma opção válida!\033[m')

# não conhecia as funções: bin, oct, hex