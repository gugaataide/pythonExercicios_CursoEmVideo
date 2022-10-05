import math
co = float(input('Quanto mede o cateto oposto?'))
ca = float(input('Quanto mede o cateto adjacente?'))
h = math.sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa desse triângulo é: {}'.format(h))