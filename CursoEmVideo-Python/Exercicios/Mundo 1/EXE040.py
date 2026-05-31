print('{:=^50}'.format(' EXE 040 '),end = '\n\n')

print('{:-^50}'.format(' Calculando a Média '))
num1 = float(input('1° nota: '))
num2 = float(input('2° nota: '))
if not (0 <= num1 <= 10 and 0 <= num2 <= 10):
    print('Notas inválidas!')
media = (num1 + num2) / 2
print(f'Media: {media:.1f}')
print('-' * 50)
if media < 5:
    print('O aluno está REPROVADO!')
elif 5 <= media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO! Parabéns!')
print(('-' * 50), end = '\n\n')

print('=' * 50)
