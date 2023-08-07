#compara dois numeros inteiros e mostra qual é o maior oou se são iguais

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))

if numero1 > numero2:
    print('o primeiro número é maior')
elif numero2 > numero1:
    print('o segundo número é o maior')
else:
    print('os dois números são iguais')