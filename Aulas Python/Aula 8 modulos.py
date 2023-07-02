#exemplo importando a biblioteca math inteira

#import math
#num = int(input('digite um numero: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a: {:.2f}'.format(num, raiz))

#exemplo importando apenas as funções utilizadas

from math import sqrt, floor

num = int( input('digite um numero: '))
raiz = sqrt(num)
print('a raiz do numero {} é igual a: {}'.format(num,floor(raiz)))