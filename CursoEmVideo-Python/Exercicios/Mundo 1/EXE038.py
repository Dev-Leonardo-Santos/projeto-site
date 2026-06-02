print('{:=^50}'.format(' EXE 038 '))

print('{:^50}'.format('Vamos comparar os números'), end = '\n\n')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo  número: '))
if n1 > n2:
    print(f'O PRIMEIRO número é maior')
elif n2 > n1:
    print(f'O SEGUNDO número é maior')
else:
    print('NÃO EXISTE número maior, os dois números são iguais.')
print(end = '\n')

print('=' * 50)
