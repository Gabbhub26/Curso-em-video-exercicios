numero = int(input('Digite um numero: '))
cont = 0
for c in range(1,numero+1):

    if numero%c == 0:
        cont+=1
        print('\033[35m', end=' ')
    else:
        print('\033[32m', end=' ')
    print(f'{c}', end=' ')

if cont == 2:

    print(f'\n\033[O número {numero} é primo')
else:
    print(f'\n\033[mo número {numero} é dívisivel por {cont} numeros e não é um número primo.')
