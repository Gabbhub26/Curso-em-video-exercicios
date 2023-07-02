# solução 1

#import math

#catop = float(input('Digite o valor do cateto oposto: '))
#catad = float(input('Digite o valor do cateto adjascente: '))
#hip = math.pow(catop, 2)+math.pow(catad, 2)
#print(' a hipotenusa é: {}'.format(math.sqrt(hip)))



#solução 2 - com biblioteca de hipotenusa

from math import hypot

catop = float(input('digite o cateto oposto: '))
catad = float(input('digite o cateto adjascente: '))
hip = hypot(catop,catad)
print('o valor da hipotenusa é: {}'.format(hip))