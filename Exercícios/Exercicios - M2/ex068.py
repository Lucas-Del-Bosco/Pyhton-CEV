print('Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')

from random import randint
from time import sleep
cont = 0
while True:
    pc = randint(0, 10)
    jg = str(input('Você quer PAR ou ÍMPAR?: ')).strip().upper()
    num = int(input('Qual número você quer?: '))
    total = pc + num
    if jg == 'PAR':
        print('Então eu sou ÍMPAR')
        print('E a soma dos nossos números é...')
        sleep(2)
        print(f'{total}')
        if total % 2 == 0:
            print('Você ganhou!')
        else:
            break
    if jg == 'ÍMPAR':
        print('Então eu sou PAR')
        print('E a soma dos nossos número é...')
        sleep(2)
        print(f'{total}')
        if total % 2 == 1:
            print('Você ganhou!')
        else:
            break
    cont += 1
print('Você perdeu!')
print(f'Você venceu {cont} vezes seguidas!')
