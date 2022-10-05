ano = int(input('Qual o ano de nascimento do atleta?'))
idade = 2021 - ano
if idade <= 9:
    print('O atleta tem {} anos é pertence a categoria Mirim.'.format(idade))
elif idade <= 14 and idade > 9:
    print('O atleta tem {} anos e pertence a categoria Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e pertence a categoria Júnior.'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e pertence a categoria Sênior.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e pertence a categoria Master.'.format(idade))

# usar biblioteca date da proxima vez
