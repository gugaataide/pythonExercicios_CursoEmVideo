l1 = []
l2 = []
l3 = []
for c in range(0,3):
    n = int(input(f'Digite um valor para [0,{c}]:'))
    l1.append(n)
for c in range(0,3):
    n = int(input(f'Digite um valor para [1,{c}]:'))
    l2.append(n)
for c in range(0,3):
    n = int(input(f'Digite um valor para [2,{c}]:'))
    l3.append(n)
print('=' * 20)
print(f'[{l1[0]}]   [{l1[1]}]   [{l1[2]}]\n'
      f'[{l2[0]}]   [{l2[1]}]   [{l2[2]}]\n'
      f'[{l3[0]}]   [{l3[1]}]   [{l3[2]}]')