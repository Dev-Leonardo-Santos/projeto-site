from datetime import date
print('{:=^50}'.format(' EXE 032 '))

ano = int(input('Qual ano quer analizar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')

print('=' * 50)
