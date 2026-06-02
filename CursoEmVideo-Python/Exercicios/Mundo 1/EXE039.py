from datetime import date

print('{:=^50}'.format(' EXE 039 '), end = '\n\n')

print('{:-^50}'.format(' ALISTAMENTO MILITAR '))
nome = input('Nome: ').title().strip()
ano_nas = int(input('ano de nascimento: '))
hoje = date.today()
ano_atu = hoje.year
idade = ano_atu - ano_nas
if idade == 18:
    print(f'{nome}, esta na hora de se alistar e servir a patria.')
    print('Se aliste IMEDIATAMENTE!')
elif idade < 18:
    dif = 18 - idade
    print('Ainda não esta na hora de se alistar.')
    print(f'Falta {dif} anos para os seu alistamento.')
    print(f'Seu alistamento vai ser em {ano_atu + dif}')
else:
    resp = input('Voce ja se apresentou para o serviço militar? [S/N] ').upper()
    if resp == 'N':
        dif = idade - 18
        print(f'Voce ja deveria ter se alistado há {dif} anos!')
        print ('Procure IMEDIATAMENTE a Junta de Serviço Militar!')
        print(f'Seu Alistamento foi em {ano_atu - dif}')
    elif resp == 'S':
        print('Voce está em dia com a pátria!')
    else:
        print('Resposta inválida. Use S ou N.')

print('-' * 50)
    
print('=' * 50)