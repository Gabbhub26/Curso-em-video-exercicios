v = input('digite algo: ')
a = v.isnumeric()
b = v.isalpha()
c = v.isspace()
d = v.istitle()

print('o tipo primitivo desta palavra é ', (type(v)))
print(' é um numero? {}\n é uma letra? {}\n é espaço? {}\n é um titulo? {}'.format(a, b, c, d))

