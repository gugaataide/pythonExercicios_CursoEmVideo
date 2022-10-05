import random
a1 = str(input('aluno:'))
a2 = str(input('aluno:'))
a3 = str(input('aluno:'))
a4 = str(input('aluno:'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem dos alunos é:')
print(lista)
