km = float(input('Qual a distância da viagem?'))
if km <= 200.0:
    p = km * 0.50
    print('Sua passagem custará: R${}'.format(p))
else:
    p = km * 0.45
    print('Sua viagem custará: R${}'.format(p))
