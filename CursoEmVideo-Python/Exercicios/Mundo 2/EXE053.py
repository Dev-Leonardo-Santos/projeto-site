print('{:=^50}'.format(' EXE 053 '))

frase = input('Digite uma frase qualquer: ')
fraseOriginal = frase
fraseF = ''.join(frase.lower().split())
tamanho = len(fraseF)
cr = -1
nao_igual = 0
for c in range(0, tamanho):
    if fraseF[c] != fraseF[cr]:
        nao_igual += 1
    cr -= 1
if nao_igual == 0:
    print('A frase é um PAlÍNDROMO ✅')
else:
    print('A frase NÃO é um PALÍNDROMO ❌')