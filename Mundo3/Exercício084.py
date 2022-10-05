n = str(input('Digite uma expressão: '))
pilha = []
for simb in n:
    if n in '(':
        pilha.append('(')
    elif n in ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válido!')
else:
    print('Inválido!')