import random
a1 = str(input('Qual o nome do primerio aluno?'))
a2 = str(input('Qual o nome do segundo aluno?'))
a3 = str(input('Qual o nome do terceio aluno?'))
a4 = str(input('Qual o nome do quarto aluno?'))
lista = [a1, a2, a3, a4]
esc = random.choice(lista)
print('O aluno escolhido foi: {}'.format(esc))

# não sabia do comando 'lista = ' no uso do random.choice