cont = 0
for c in range(0,6):
    numero = int(input('Escreva um numero: '))
    if numero%2 == 0:
        cont = cont + numero
print(cont)