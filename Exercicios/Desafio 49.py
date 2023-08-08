numero = int(input('Qual numero você quer saber a tabuada? '))

for c in range(0, 11):
    print(f'{numero} x {c} = {numero*c}')