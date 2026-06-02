print('{:=^50}'.format(' EXE 056 '))

maisVelho = float('-inf')
Mulher_nova = 0
soma_idade = 0
print('{:-^50}'.format(' Analizador '))
for c in range (1, 5):
    print(f'({c}) ---')
    #Validando nome
    nome = input('Nome: ').title().strip()
    if not nome.replace(' ', '').isalpha():
        print('Esse nome NÃO É VALIDO!')
    #validando idade
    idade = int(input('Idade: '))
    if idade > 150:
         print('Idade INVALIDA. Ninguem é tão velho assim!')
    #validando sexo
    sexo = input('sexo [M/F]: ').upper().strip()
    if not (sexo == 'M' or sexo == "F"):
         print('Apenas Feminino ou Masculino')
    #Somando as idades para fazer a media
    soma_idade += idade
    if sexo == "M":
        #Nome do homem mais velho
         if idade > maisVelho:
                maisVelho = idade
                nome_velho = nome
    elif sexo == 'F':
        #Total de mulheres com menos de 20 anos
         if idade < 20:
              Mulher_nova += 1
    print('-' * 50)
print(f'A média de idade do grupo é de {round(soma_idade / 4)}')
print(f'O nome do homem mais velho é {nome_velho}') if maisVelho != float('-inf') else print('Nenhum homem foi cadastrado')
if Mulher_nova == 0:
     print('Neste grupo, não tem mulheres com menos de 20 anos.')
elif Mulher_nova == 1:
     print(f'Neste grupo tem apenas {Mulher_nova} mulher com menos de 20 anos.')
else:
     print(f'Neste grupo tem {Mulher_nova} mulheres com menos de 20 anos ')