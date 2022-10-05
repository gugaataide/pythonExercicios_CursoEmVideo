valor = float(input('Qual o valor do imóvel?'))
sal = float(input('Qual o seu salário?'))
anos = int(input('Em quantos anos você deseja financiar o imóvel?'))
parc = valor / (anos * 12)
print('\033[1;33m O valor de cada prestação é: R${:.2f}\033[1;33m '.format(parc))
if parc > (sal * 0.30):
    print('\033[1;31m Infelizmente seu financiamento foi negado, pois a parcela é superior a 30% do seu salário\033[m')
else:
    print('\033[1;32m Parabéns, seu crédito foi aprovado!\033[m')
