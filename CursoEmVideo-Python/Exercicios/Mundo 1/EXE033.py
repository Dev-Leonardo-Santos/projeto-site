print('{:=^50}'.format(' EXE 033 '))

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo  Valor: '))
num3 = int(input('Terceir  valor: '))

if num1 > num2 and num1 > num3:
    maior = num1 
    if num2 < num3:
        menor = num2
    else:
        menor = num3
elif num2 > num3 and num2 > num3:
    maior = num2
    if num3 > num1:
        menor = num1
    else:
        menor = num3
else:
    maior = num3
    if num2 < num1:
        menor = num2
    else:
        menor = num1
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')

print('=' * 50)
