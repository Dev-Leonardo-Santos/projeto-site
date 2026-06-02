print('{:=^50}'.format(' EXE 028 '))

velo = float(input('Qual é a velocidadea arual do carro? '))
if velo >80:
    print('Multado! Voce excedeo o limite permitido que é de 80 km/h!')
    multa = (velo - 80) * 7
    print(f'Voce deve pagar R${multa:.2f} de multa!')
print('Boa viagem! Dirija com segurança!')

print('=' * 50)
