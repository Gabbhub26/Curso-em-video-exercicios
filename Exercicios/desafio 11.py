

l = float(input('largura: '))
h = float(input('altura: '))
t = str(input('marca: '))
ti = 1

if t == 'suvinil':
    ti=3
    print(f'você precisa de {qt:.2f} litros de tinta para pintar a parede')
elif t == 'coral':
    ti=2
    print(f'você precisa de {qt:.2f} litros de tinta para pintar a parede')
else:
    print('marca não cadastrada. Consulte o fabricante')


a = l*h
qt = a/ti

#print(f'você precisa de {qt:.2f} litros de tinta para pintar a parede')
