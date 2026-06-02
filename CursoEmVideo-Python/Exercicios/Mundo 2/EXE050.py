print('{:=^50}'.format(' EXE 050 '), end='\n\n')

cont_par = 0
for c in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        cont_par = cont_par + num
if cont_par == 0:
    print('Você digitou nenhum numero PAR!')
else:
    print(f'A soma dos valores pares é {cont_par}')
print()
print('=' * 50)
