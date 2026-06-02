print('{:=^50}'.format(' calculo Area m² para tinta '))
largura = float(input('valor largura: '))
compri = float(input('valor do comprimento: '))
area = largura * compri
tinta = area / 2
print(f'A sua parede mede {area:.1f}²m\nE precisara de {tinta:.1f} litros de tinta para pintar')
print('=' * 50)