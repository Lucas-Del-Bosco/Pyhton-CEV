print('Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.')

from random import randint
pc = randint(0, 10)
jogador = int(input('Digite um número de 0 a 10: '))
palpites = 1
while jogador != pc:
    if jogador > pc:
        jogador = int(input('Menos... Tente novamente: '))
    elif pc > jogador:
        jogador = int(input('Mais... Tente novamente: '))
    palpites += 1
print(f'Você conseguiu! Só precisou de {palpites} tentativas.')
