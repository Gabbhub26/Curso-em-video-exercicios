#este programa converte um numero de base decimal em binario, octal ou hexa a depender da opção escolhida pelo usuario


numero_conv = int(input('digite o numero decimal a ser convertido: '))
opcao = int(input('\n2-base binaria\n8-base octa\n16-base hexa\n\n'))

if opcao == 2:
    print(f'numero {numero_conv} binário ',bin(numero_conv))
elif opcao == 8:
    print(f'numero {numero_conv} octa: ',oct(numero_conv))
elif opcao == 16:
    print(f'numero {numero_conv} hexa: ',hex(numero_conv))
else:
    print('base não cadastrada.')