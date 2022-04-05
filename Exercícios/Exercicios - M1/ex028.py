print('Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.\nO programa deverá escrever na tela se o usuário venceu ou perdeu.')

from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jg = int(input('Em que número pensei?: '))
print('PROCESSANDO...')
sleep(2)
if jg == pc:
    print('Parabéns, você me venceu!')
else:
    print('Tente novamente da próxima vez, lixo!')

