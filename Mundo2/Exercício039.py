an = int(input('Em que ano você nasceu?'))
idade = 2021 - an
if idade > 18:
    print('Você tem {} anos, e por isso seu alistamento está {} ano(s) atrasado'.format(idade, idade - 18))
elif idade < 18:
    print('Você tem {} anos, e por isso falta(m) {} ano(s) para você se alistar!'.format(idade, 18 - idade))
else:
    print('Você tem 18 anos, e por isso deve se alistar imediatamente!')
print('Seu alistamento será em {}!,3'.format(an + 18))