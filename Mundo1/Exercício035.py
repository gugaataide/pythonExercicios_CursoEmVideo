sal = float(input('Qual o seu salário?'))
if sal > 1250:
    aum = sal + (sal * 0.10)
else:
    aum = sal + (sal * 0.15)
print('Seu novo salário, após o aumento é de: R${}'.format(aum))