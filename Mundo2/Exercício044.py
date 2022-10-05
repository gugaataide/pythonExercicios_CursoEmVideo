val = float(input('Qual o valor do produto?R$'))
fdp = int(input('[1] A vista /Dinheiro ou Cheque \n [2] A vista (cartão) \n [3] 2x no cartão '
                '\n [4] 3x ou mais no cartão \nQual a forma de pagamento?'))
if fdp == 1:
    print('O valor para pagamentos a vista no dinheiro ou cheque é: R${}'.format(val - (val * 0.10)))
elif fdp == 2:
    print('O valor para pagamentos a vista no cartão de crédito é: R${}'.format(val - (val * 0.05)))
elif fdp == 3:
    print('O valor para pagamentos em 2x no cartão de crédito é: R${}'.format(val))
elif fdp == 4:
    parc = int(input('Em quantas parcelas você deseja pagar?'))
    print('O valor para pagamentos em 3x ou mais no cartão de crédito é: R${}'.format(val + (val * 0.20)))
    print('E cada parcela ficará no valor de: R${}'.format((val + (val * 0.20)) / parc))
