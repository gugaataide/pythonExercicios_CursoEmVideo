nome = str(input('Digite seu nome:')).strip()
sp = nome.split()
spf = len(sp)
print('Prazer em conhecê-lo, {}! \nSeu primeiro nome é: {} \n Seu último nome é: {}'.format(nome, sp[0], sp[spf - 1]) )

#precisei de ajuda para mostrar o último nome