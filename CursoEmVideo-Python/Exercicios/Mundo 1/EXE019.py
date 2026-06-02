import random

print('{:=^50}'.format(' ALUNO ALEATORIO'))
aluno_1 = input('aluno 1 : ')
aluno_2 = input('aluno 2: ')
aluno_3 = input('aluno 3: ')
aluno_4 = input('aluno 4: ')
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

print('\no aluno escolhido para apagar o quadro foi', random.choice(alunos))
print('\nA ornde da apresentação:')

print('=' * 50)
