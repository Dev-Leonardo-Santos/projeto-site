print('{:=^50}'.format(' EXE 044 '),end='\n\n')

valor_compra = float(input('Qual o valor do produto? R$'))
compra = int(input('''Qual a formar de pagamento? 
[1] À vista no DINHEIRO/ PIX
[2] À vista no CARTÂO
[3] No CREDITO PARCELADO
 R: '''))
if compra == 1:
    valor_final = valor_compra - (valor_compra * 10/100)
elif compra == 2:
    valor_final = valor_compra - (valor_compra * 5/100)
elif compra == 3:
    print('-' * 50)
    parcelas = int (input('Em quantas parcelas? R:'))
    if parcelas == 2 or  parcelas == 3:
        valor_final = valor_compra
        print(f'O valor das parcelas ficara {valor_final / parcelas:.2f}')
    elif parcelas == 1:
        valor_final = valor_compra - (valor_compra * 5/100)
    else:
        valor_final = valor_compra + (valor_compra * 20/100)
        print(f'O valor das parcelas ficara {valor_final / parcelas:.2f}')
else:
    print('NÚMERO INVALIDO. Recomece a operação!')
print(f'O total a se pagar sera de R${valor_final:.2f}')
print('=' * 50)