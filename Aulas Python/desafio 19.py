import random
n1 = input('aluno 1:')
n2 = input("aluno 2: ")
n3 = input('aluno 3:')
n4 = input('aluno 4:')

nomes = [n1,n2,n3,n4]

print('vencedor {}'.format(random.choice(nomes)))