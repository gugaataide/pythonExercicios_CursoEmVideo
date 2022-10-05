L = float(input('Qual a largura da parede?'))
A = float(input('Qual a altura da parede?'))
area = L*A
litros = area/2
print('Sua parede tem {}x{} metros e possui {} m²'.format(L, A, area))
print('E você precisará de {} litros de tinta!'.format(litros))
