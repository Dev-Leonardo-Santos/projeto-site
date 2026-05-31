print('{:=^30}'.format(' BOLETIM '))

n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
m = (n1 + n2) /2

print(f'a media das notas {m:.1f}')
print('=' * 30)
if m > 7.5:
    print('parabens, voce mandou bem! esta aprovado')
elif m >= 6:
    print('voce esta aprovado, parabens!')
elif m == 5:
    print('Voce esta de rescuperação!')
else:
    print('REPROVADO!')