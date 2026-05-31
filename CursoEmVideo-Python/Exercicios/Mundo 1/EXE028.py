from random import randint
from time import sleep

print('{:=^50}'.format(' EXE 028 '), end = '\n\n')
na = randint(0, 5)

print('{:-^50}'.format(' JOGO DO ADIVINHA '))
r = int(input('Diga um numero de 0 a 5: '))
sleep(2)
if r == na:
    print('PARABENS! Voce acertou!')
    print(f'O numero sorteado foi {na}')
    print(('-' * 50), end='\n')
    print('Parece que a sorte esta com você. Porque não joga na loteria?', end='\n\n')
else:
    print('Tente na proxima, nessa voce errou!')
    print(f'O numero sorteado foi {na}')
    print(('-' * 50), end='\n')
    print('Não perca as suas esperanças, vai que a próxima acerta',end='\n\n')
print('=' * 50)
