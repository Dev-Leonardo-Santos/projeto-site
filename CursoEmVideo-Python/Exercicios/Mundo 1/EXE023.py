print('{:=^50}'.format(' EXE 023 '))

num = int(input('Digite um número: '))
print('Analizando...')

u = num % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = num // 1000 

print('-' * 50)

print(f'Unidade  [{u}]')
print(f'Dezena   [{d}]')
print(f'Centena  [{c}]')
print(f'Milhar   [{m}]')

print('-' * 50)
print('FIM!')
print('=' * 50)
