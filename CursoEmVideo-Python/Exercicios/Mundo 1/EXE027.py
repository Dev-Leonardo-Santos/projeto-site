print('{:=^50}'.format(' EXE 027 '))

nome = input('Digite seu nome completo: ').strip().title()
print('Muito prazer em te conhecer!')
nq = nome.split()
print(f'Seu primeiro nome é {nq[0]}')
print(f'Seu último nome é {nq[-1]}')

print('=' * 50)
