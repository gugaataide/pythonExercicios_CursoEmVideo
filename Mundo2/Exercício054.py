from datetime import date
adultos = 0
dimenores = 0
for c in range (0, 7):
    an = int(input('Qual o ano do seu nascimento?'))
    idade = date.today().year - an
    if idade >= 18:
        adultos = adultos + 1
    else:
        dimenores = dimenores + 1
print('No grupo há {} adultos\nE {} menores de idade'.format(adultos, dimenores))