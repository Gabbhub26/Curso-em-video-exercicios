#programa que leia duas notas de um aluno media 5 = reprovado, media 5 a 6,9 recuperação e acima de 7 aprovado

nota1 = float(input('nota no primeiro semestre: '))
nota2 = float(input('nota no segundo semestre: '))

media = (nota1+nota2)/2

if media <= 5.0:
    print(f'Média {media}.\naluno reprovado.')
elif media > 5.0 and media < 7.0:
    print(f'Média {media}.\naluno em recuperação.')
else:
    print(f'Média {media}.\nAluno aprovado.')