s = str(input('Qual o seu sexo [M/F]? ')).strip().lower()
while s != 'm' and s != 'f':
    s = str(input('erro, digite novamente: ')).strip().lower()
print('Entendi!')