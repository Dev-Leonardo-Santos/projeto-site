print('{:=^50}'.format(' EXE 055 '))

pesado = float('-inf')
leve = float('inf')
for c in range(1, 6):
    pe = float(input(f'{c}° pessoa: Kg '))
    if pe > pesado:
        pesado = pe
    if pe < leve:
        leve = pe
print(f'O MAIOR peso registrado foi de Kg {pesado}')
print(f'O MENOR peso registrado foi de kg {leve}')
