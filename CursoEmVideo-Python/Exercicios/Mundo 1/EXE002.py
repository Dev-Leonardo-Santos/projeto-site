nome = input('Qual o seu nome?: ')
print(f'É um prazer te conhecer, {nome}!')
if nome.lower() == 'alice':     
    print('voce não esta no pais das maravilhas!')
elif nome.lower() == 'leonardo' or nome.lower() == 'leo':
    print('voce vai ser um grande programador!')
else :
    print('bem vindo ao mundo do python!')