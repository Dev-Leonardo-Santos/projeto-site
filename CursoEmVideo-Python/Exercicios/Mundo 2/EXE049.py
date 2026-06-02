print('{:=^50}'.format(' EXE 049 '), end='\n\n')
print('{:-^50}'.format(' Tabuada '))

try:
    num = int(input('Digite um numero: '))
    for c in range(0, 11):
        print(f'{num} x {c} = {num * c}')
except ValueError:
    print('Digite apenas numeros inteiros!')

print(('-' * 50), end='\n\n')
print('=' * 50) 
