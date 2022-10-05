n1 = float(input('Qual foi a sua primeira nota?'))
n2 = float(input('Qual foi a sua segunda nota?'))
n3 = float(input('Qual foi a sua terceira nota?'))
m = (n1 + n2 + n3) / 3
if m >= 7.0:
    print('\033[1;32m Sua média foi {} e você foi APROVADO!\033[m'.format(m))
elif m >= 5.0 and m < 7.0:
    print('\033[1;33m Sua média foi {:.2f} e você ficou de RECUPERAÇÃO!\033[m'.format(m))
elif m >= 0.0 and m < 5.0 :
    print('\033[1;31m Sua média foi {} e você foi REPROVADO!\033[m'.format(m))
else:
    print('Erro! você inseriu notas incorretas. tente novamente')