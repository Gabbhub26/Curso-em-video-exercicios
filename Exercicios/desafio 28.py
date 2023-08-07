import random

numero = random.randint(1,5)
print(numero)
chute = float(input('qual numero eu pensei? '))

if chute == numero:
        print('Parabéns você chutou bem! ')
else:
        print('Que pena! Você errou. ')

print('obrigado por brincar comigo')