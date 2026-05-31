print('{:=^50}'.format(' EXE 051 '), end='\n')

print('{:-^50}'.format(' Progressão Aritmética '))
inicio = int(input('Diga o inicio da progressão: '))
razao = int(input('Diga a razão: '))
pa = inicio

print('- ' * 25)
for c in range(1, 11):
    print(f'{c}° = {pa}')
    pa += razao
print('=' * 50)
