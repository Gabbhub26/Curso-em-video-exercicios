print('{:=^40}'.format('LOJAS MONTEIRO&SOUZA'))

valor = float(input('Valor das compras: R$'))
print('FORMAS DE PAGAMENTO\n[1]À vista dinheiro ou pix\n[2]À vista cartão de crédito\n[3]2x no cartão de crédito\n[4]3x ou mais no cartão de crédito')

opcao = int(input('qual a opção? '))

if opcao == 4:
    parcelas = int(input('numero de parcelas: '))

if opcao == 1:
    print(f'sua compra sairá de R${valor} por R${valor-(valor*5/100)} ')
elif opcao == 2:
    print(f'sua compra sairá de R${valor} por R${valor+(valor*2/100)}')
elif opcao == 3:
    print(f'sua compra sairá de R${valor} por R${valor+(valor*2.5/100)}')
elif opcao == 4:
    print(f'sua compra sairá de R${valor} por R${valor+((valor*1.5/100)*parcelas)}')
else:
    print('\nForma de pagamento não cadastrada.')
