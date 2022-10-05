s1 = float(input('Digite um segmento:'))
s2 = float(input('Digite outro segmento:'))
s3 = float(input('Digite mais um segmento:'))

if s1 < s2 + s3 and s2 < s1 + s2 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Estes segmentos podem formar um triângulo equilátero!')
    elif s1 == s2 or s3 == s1 or s2 == s3:
        print('Esses segmentos podem formar um triângulo isóceles!')
    elif s1 != s2 != s3:
        print('Estes segmentos podem formar um triângulo escaleno!')
else:
    print('Esses segmentos não formam um triângulo!')

# troquei and por or