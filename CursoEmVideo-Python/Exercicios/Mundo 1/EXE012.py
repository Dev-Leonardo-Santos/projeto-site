print('{:=^50}'.format('Calculo Desconto'))

preço = float(input('Preço R$: '))
por_desc = float(input('desconto %: '))
porce = por_desc / 100 
va_desc = preço * porce
preço_f = preço - va_desc

print(f'O desconto foi de R${va_desc:.2f}\nE o total a pagar é R${preço_f:.2f}')
print('=' * 50)
