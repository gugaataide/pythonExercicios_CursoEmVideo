vel = int(input('Qual a velocidade do carro?'))
if vel > 80:
    am = (vel - 80) * 7
    print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE, e deve pagar uma multa de R${}'.format(am))

else:
    print('Parabéns, você passou na velocidade correta!')