print('{:=^50}'.format(' EXE 048 '))

soma = 0
conta = 0

for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            soma = soma + c
            print((c), end=' ')
            conta += 1
            if conta % 10 == 0:
                print()
print()
print(f'A soma entre o valores acima é de {soma}')
print('=' * 50)
