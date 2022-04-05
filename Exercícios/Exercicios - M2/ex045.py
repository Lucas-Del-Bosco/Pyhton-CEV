print('Crie um programa pra jogar jokenpô com você')
print('-=-' * 20)
print('             VAMOS JOGAR PEDRA, PAPEL E TESOURA?')
print('-=-' * 20)
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
r = randint(0, 2)
pc = itens[r]
print('''Escolha uma das opções a seguir:
[1] Pedra
[2] Papel
[3] Tesoura''')
opção = int(input('Digite o número correspondente: '))
if pc == 'Tesoura':
    print(f'Eu escolhi {pc}')
    if opção == 1:
        print('Parabéns, você venceu dessa vez.')
    elif opção == 2:
        print('Não foi dessa vez, tente novamente.')
    elif opção == 3:
        print('Parece que empatamos.')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 'Papel':
    print(f'Eu escolhi {pc}')
    if opção == 1:
        print('Não foi dessa vez, tente novamente.')
    elif opção == 2:
        print('Parece que empatamos.')
    elif opção == 3:
        print('Parabéns, você venceu dessa vez.')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 'Pedra':
    print(f'Eu escolhi {pc}')
    if opção == 1:
        print('Parece que empatamos.')
    elif opção == 2:
        print('Parabéns, você ganhou dessa vez.')
    elif opção == 3:
        print('Não foi dessa vez que você conseguiu, tente novamente.')
    else:
        print('JOGADA INVÁLIDA')

