print('{:=^50}'.format(' EXE 043 '), end='\n\n')

print('{:-^50}'.format('Calculando IMC'))
altura = float(input('altura (m): '))
peso = float(input('Peso (kg): '))
imc = peso / (altura * altura)
print((f'O IMC dessa pessoa é de {imc:.1f} '), end='')
if imc < 18.5:
  print('e está abaixo do peso')
elif imc < 25:
  print('e está no peso ideal')
elif imc < 30:
  print('e está em sobrepeso')
elif imc < 40:
  print('e está em obesidade')
else:
  print('e está em Obesidade mórbida')
print(('-' * 50), end='\n')
print('=' * 50)