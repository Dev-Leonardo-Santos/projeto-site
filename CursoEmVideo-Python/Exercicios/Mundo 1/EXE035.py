print('{:=^50}'.format(' EXE 035 '), end = '\n\n')

print('{:-^50}'.format('Analizador de Triangulos'))
a = float(input('Primeiro segmento: '))
b = float(input('Segundo  segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmento acima NÃO PODEM FORMAR triângulo')
print(('-' * 50), end = '\n\n')

print('=' * 50)
