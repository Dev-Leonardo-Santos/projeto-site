import random
print('{:=^50}'.format(' EXE 045 '))

maquina = random.choice(['pedra','papel','tesoura'])
print('{:-^50}'.format(' JOGO JOKENPÔ '), end='\n\n')
jogador = int(input('''Escolha a sua jogada:
[1] Pedra
[2] Papel
[3] Tesoura
R: '''))
# JOGADAS ERROR
if not (jogador == 1 or jogador == 2 or jogador == 3 ):
    print('JOGADA ERRADA! Não existe essa jogada.')
# JOGADAS EMPATE
if((maquina == 'pedra' and jogador == 1) or (maquina == 'papel' and jogador == 2) or (maquina == 'tesoura' and jogador == 3)):
    print('EMPATE')
# JOGADAS JOGADOR VITORIA
elif((maquina == 'pedra' and jogador == 2) or (maquina == 'papel' and jogador == 3) or (maquina == 'tesoura' and jogador == 1)):
    print('VITORIA DO JOGADOR')
else:
    print('VITORIA DA MAQUINA')
print(('-' * 50), end='\n')
print('=' * 50)