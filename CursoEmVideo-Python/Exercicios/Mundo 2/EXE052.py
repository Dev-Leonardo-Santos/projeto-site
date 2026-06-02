print('{:=^50}'.format(' EXE 052 '), end='\n\n')

contDiv = 0
print('{:-^50}'.format(' É um número primo ? '))
num = int(input('Diga um número inteiro: '))
for c in range(2, num):
    if num % c == 0:
        contDiv += 1
if contDiv == 0:
    print(f'O número {num}, É UM NÚMERO PRIMO ✅', end='\n\n')
else:
    print(f'O número {num}, NÃO É UM NÚMERO PRIMO ❌', end='\n\n')
print('=' * 50)
