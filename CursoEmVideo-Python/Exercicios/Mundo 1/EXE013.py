print('{:=^50}'.format(' Almento salarial '))

salario = float(input('Salario: R$'))
novo_salario = salario + ((15/100)*salario)

print(f'Voce recebera 15% de almento salarial, Parabens!\nSeu novo salario vai ser: R${novo_salario:.2f}')
print('=' * 50) 