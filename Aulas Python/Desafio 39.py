#programa que le a data de nascimento de um jovem e diz se ainda falta tempo para ele se alisatar, se ja está na hora ou se ja passou o tempo

import datetime

data_atual = datetime.date.today().year

ano_nascimento = int(input('qual seu ano de nascimento: '))
sexo = str(input('seu sexo: '))

idade = data_atual-ano_nascimento
alistamento = 18-idade
if sexo == 'masculino':
    if idade < 18:
        print(f'você tem apenas {idade}  anos \nainda faltam {alistamento} anos para você se alistar!')
    elif idade == 18:
        print(f'você fez {idade} anos \nVá até a junta militar mais proxima e se aliste!')
    else:
        print(f'você tem {idade} \ndeveria ter se alistado há {alistamento*(-1)} anos, em {ano_nascimento+18}. \nProcure a junta militar mais próxima e regularize sua situação!')
else:
    print('você não precisa se alistar.')
print('\nExercito Brasileiro: Braço forte, Mão amiga.')