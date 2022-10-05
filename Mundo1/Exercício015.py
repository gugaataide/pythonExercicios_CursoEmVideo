km = float(input('Quantos kilômetros foram percorridos?'))
d = int(input('Quantos dias você usou o carro?'))
ppd = d*60
ppkm = km*0.15
pt = ppd + ppkm
print('Total a pagar R${:.2f}'.format(pt))