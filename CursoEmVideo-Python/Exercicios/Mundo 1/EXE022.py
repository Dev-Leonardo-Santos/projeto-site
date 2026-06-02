print('{:=^50}'.format(' EXE 022 '))

nome = input('Nome: ').strip()

nome_sem_espaco = ''.join(nome.split())
primeiro_nome = nome.split()[0]

print(f'Seu nome em maiúsculo é {nome.upper()}')  #nome maiúsculo
print(f'seu nome em minúsculo é {nome.lower()}')  #nome Minúsculo
print(f'Seu nome tem ao todo {len(nome_sem_espaco)} letras') #quantos caracteres sem espaços
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')  #Quantas letras tem o primeiro nome 
print(f'A primeira letra do seu nome é {nome[0]}')

print('=' *50)