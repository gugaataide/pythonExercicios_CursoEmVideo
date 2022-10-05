num = int(input('Digite um número de 0 a 9999:'))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print ('Analisando seu numero, observamos que ele possui: \n Unidades: {} \n Dezenas: {} \n Centenas: {} \n Milhares:{}'.format(uni, dez, cen, mil))


#precisei de ajuda por motivos matemáticos