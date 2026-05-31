from random import shuffle as sf


print('{:=^50}'.format(' EXE 020 '))
a1 = input('Primeiro luno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]
sf(alunos)
print(f'A ordem de apresentação é: \n{alunos}')

print('=' * 50)
 