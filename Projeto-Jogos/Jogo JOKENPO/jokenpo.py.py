import random
import time

print('{:=^50}'.format(' EXE 045 '))

jogadas = {
    1 : 'pedra',
    2 : 'papel',
    3 : 'tesoura'
}

escolha_maquina = random.choice(list(jogadas.keys()))
maquina = jogadas[escolha_maquina]
print('{:-^50}'.format(' JOGO JOKENPÔ '), end='\n\n')
print('Escolha a sua jogada:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
player = int(input('R: '))

# JOGADAS ERROR
if not (player == 1 or player == 2 or player == 3 ):
    print('JOGADA ERRADA! Não existe essa jogada.')
    print(('-' * 50), end='\n')
# JOGADAS EMPATE
elif(player == maquina):
    mensagem = ('O jogo deu EMPATE 🤝')
# JOGADAS JOGADOR VITORIA
elif(player == 1 and maquina == 3) or \
    (player == 2 and maquina == 1) or \
    (player == 3 and maquina == 2):
    mensagem = ('VOCÊ GANHOU! 🎉')
else:
    mensagem = ('Voce perdeu. Persista e não desisti!')

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print(('PO!!!'), end='\n')

print('- ' * 25)
print(f'MAQUINA: {maquina}')
print(F'JOGADOR: {player}')
print(mensagem)
print(('- ' * 25), end='\n')
print('=' * 50)