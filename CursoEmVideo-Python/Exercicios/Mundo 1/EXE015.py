dias = int(input('quantos dias alugados: '))
km = float(input('quantos KM rodados: '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pago:.2f}')
