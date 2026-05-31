print('{:=^50}'.format(' EXE 008 '))
metros = float( input('Uma distãncia em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = int(metros * 10)
cm = int(metros * 100)
mm = int(metros * 1000)

print(f'A medida de {metros}m coresponde a')
print(f'{km}km\n{hm}hm\n{dam}dam\n{dm} dm\n{cm} cm\n{mm} mm')
print('=' * 50)
