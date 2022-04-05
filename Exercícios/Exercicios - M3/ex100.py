#print('Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.')

from random import randint
from time import sleep


def sorteio(lista):
    print('~~' * 10)
    print('SORTEANDO 5 VALORES: ')
    print('~~' * 10)
    sleep(1)
    for c in range(1, 6):
        num = randint(1, 10)
        print(num, end=' ')
        sleep(0.5)
        lista.append(num)
    print()
    print('~' * 20)


def somapar(lista):
    soma = 0
    for valor in números:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares de {números} é {soma}!')


números = list()
sorteio(números)
somapar(números)
