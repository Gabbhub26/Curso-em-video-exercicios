import datetime

nascimento = int(input('ano de nascimento: '))

data_atual = datetime.date.today().year

idade_atleta = data_atual-nascimento

if idade_atleta <= 9:
    print(f'o atleta tem {idade_atleta} anos.\nAtleta mirim.')
elif idade_atleta > 9 and idade_atleta <= 14:
    print(f'o atleta tem {idade_atleta} anos.\nAtleta infantil.')
elif idade_atleta > 14 and idade_atleta <= 19:
    print(f'O atleta tem {idade_atleta} anos.\nAtleta Junior.')
elif idade_atleta > 19 and idade_atleta <= 20:
    print(f'O atleta tem {idade_atleta} anos. \nAtleta Senior.')
else:
    print(f'O atleta tem {idade_atleta} anos.\nAtleta Master.')