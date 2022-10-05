palavras = ('açucar', 'carvao', 'hax', 'playstation')
for vog in palavras:
    print(f'\nNa palavra {vog} temos as vogais: ', end='' )
    for cada in vog.lower():
        if cada in 'aeiou':
            print(cada.upper(), end=' ')