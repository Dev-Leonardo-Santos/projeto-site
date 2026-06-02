print('{:=^50}'.format(' EXE 0 31 '))

km = float('Qual é a distâcia da sua viagem? ')
print(f'Você está preste a começar uma viagem de {km:.1f}km')
if km <=200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print(f'E o preço da sua passagem será de R${passagem:.2f}')

print('=' * 50)
