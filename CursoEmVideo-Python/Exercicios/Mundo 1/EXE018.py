from math import radians,sin, cos, tan
print('{:=^50}'.format(' SENO E COSSENO '))

numero_graus = float(input('diga um numeros em graus: '))
seno = sin(radians(numero_graus))
coss = cos(radians(numero_graus))
tang = tan(radians(numero_graus))

print(f'\nO valor do seno de {numero_graus}° é de {seno:3f}')
print(f'E o valor do cosseno é de {coss:3f}')
print(f'e o valor da tangente é de {tang:3f}')

print('=' * 50)     