from datetime import datetime

print('{:=^50}'.format(' EXE 054 '))
agora = datetime.now()
maior = 0
menor = 0
for c in range(1, 8):
    anoA = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if (agora.year - anoA) < 18:
        menor += 1
    else:
        maior += 1
print('- ' * 25)
print(f'{maior} pessoa atingiu a maioridade') if maior == 1 else print(f'{maior} pessoas atingiram a maioridade') 
print(f'{menor} pessoa NÃO atingiu a maioridade') if menor == 1 else print(f'{menor} pessoas NÃO atingiram a maioridade')
