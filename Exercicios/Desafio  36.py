#programa que aprova ou reprova financiamento imobiliario. O programa pergunta valor da casa, salário e em quantos anos pretende pagar. O valor da parcela não pode exceder 30% do valor do salário

valor_casa = float(input('Valor do imóvel: R$'))
renda_familiar = float(input('Renda familiar: R$'))
prazo = int(input('Prazo para pagamento (em meses): '))
#entrada = int(input('valor da entrada: '))

prestacao_mensal = valor_casa/prazo

print(f'prestação mensal:{prestacao_mensal}')

if prestacao_mensal <= renda_familiar*30/100:
    print('Parabéns! Seu crédito foi aprovado. Em breve o gerente entrará em contato.')
else:
    print('Seu credito não foi aprovado')