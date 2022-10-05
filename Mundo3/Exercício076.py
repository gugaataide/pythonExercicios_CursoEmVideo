preços = ('Calabresa', 40.99,
          'macarrão', 3.99,
          'leite', 10.99,
          'ovos', 10.00,
          'carne moída', 24.99)
print('=' * 40)
print(f'{"Mercadão Atayde":^40}')
print('=' * 40)
for cada in range(0, len(preços)):
    if cada % 2 == 0:
        print(f'{preços[cada]:.<30}', end='')
    else:
        print('R$', preços[cada])