from random import randint

print('{:=^35}'.format('PEDRA, PAPEL OU TESOURA'))
print('='*35)

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print('''[0]Pedra
[1]Papel
[2]Tesoura''')

print(pc)

jogador = int(input('Escolha uma opção: '))


if pc == 0:
    if jogador == 0: print('Empate!')
    elif jogador == 1: print('Você Ganhou! Parabéns!')
    elif jogador == 2: print('Que pena! Você perdeu!')
    else: print('opcao invalida')
elif pc == 1:
    if jogador == 1: print('Empate!')
    elif jogador == 2: print('Você Ganhou! Parabéns!')
    elif jogador == 0: print('Que pena! Você perdeu!')
    else: print('opcao invalida')
elif pc == 2:
    if jogador == 2: print('Empate!')
    elif jogador == 0: print('Você Ganhou! Parabéns!')
    elif jogador == 1: print('Que pena! Você perdeu!')
    else: print('opcao invalida')
print('obrigado por jogar!')
