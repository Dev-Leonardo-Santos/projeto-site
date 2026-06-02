print('{:=^50}'.format(' EXE 026 '))

frase = input('Digite uma frase: ').strip().lower()
print(f'A letra A aparece {frase.count('a')} na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('a')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('a')+1}')

print('=' * 50)
