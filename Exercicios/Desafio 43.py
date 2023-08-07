peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))
IMC = peso/altura**2

print('seu IMC: ', IMC)

if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC >= 18.6 and IMC < 25:
    print('Você está no peso ideal.')
elif IMC >= 25 and IMC < 30:
    print('Você está levemente acima do peso.')
elif IMC >= 30 and IMC < 35:
    print('Obesidade grau 1')
elif IMC >= 35 and IMC < 40:
    print("Obesidade grau 2.")
else:
    print('Nível Thais Carla')