nome = str(input('Qual seu nome completo? ')).strip()
maiusculas = nome.upper()
minusculas = nome.lower()

#palavras = len(nome.split())
#letras = palavras*(len(nome))



print(f'''esses são os dados do seu nome:
nome em letras maiúsculas:{maiusculas}
nome em letras minusculas: {minusculas}
quantidade total de letras do nome completo: {(len(nome)-(len(nome.split())-1))}
quantidade de letras primeiro nome: {len(nome.split()[0])}
''')


