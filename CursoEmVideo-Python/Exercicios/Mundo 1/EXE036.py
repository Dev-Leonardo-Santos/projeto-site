print('{:=^50}'.format(' EXE 036 '), end = '\n\n')

print('{:-^50}'.format('EMPRÉSTIMO BANCARIO'))
valor_casa = float(input('Qual o valor do empréstimo? R$'))
salario = float(input('informe os seu salario: R$'))
tempo_ano_pagar = int(input('Em quantos anos pretende pagar? '))
parcela = valor_casa / (tempo_ano_pagar * 12)
if salario * (30 / 100) >= parcela:
    print('- ' *25)
    print('Seu empréstimo foi aprovado, PARABÉNS!')
    print(f'Serão {tempo_ano_pagar * 12} parcelas de R${parcela:.2f} a se pagar.')
    print('- ' * 25)
else:
    print('- ' * 25)
    print(f'''Seu emprestimo foi NEGADO!'
O seu salario é imcopativel, exede o limite de 30% por parcela!
O valor da parcela ficaria R${parcela:.2f}''')
    print('- ' * 25)
print(('-' * 50), end = '\n\n')

print('=' * 50)
