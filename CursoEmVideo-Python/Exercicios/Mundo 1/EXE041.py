from datetime import date

print('{:=^50}'.format(' EXE 041 '))

dtn_atleta = input('Data de nascimento [dd/mm/aaa]: ').split('/')
ano_atual = date.today().year
idade = ano_atual - (int(dtn_atleta[2]))
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JúNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'O atleta com {idade} anos irá participar da categoria {categoria}.')

print('=' * 50)
