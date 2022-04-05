#print('Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.')

from time import sleep


def maior(* num):
    cont = mai = 0
    print('=-' * 20)
    print(f'Analisando os valores passados...')
    sleep(1)
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
        if cont == 0:
            mai = c
        if c > mai:
            mai = c
        cont += 1
    print()
    print(f'Foram analisados {cont} números ao todo!')
    print(f'O maior valor inforamdo foi {mai}!')


maior(2, 5, 6, 8, 3, 9)
maior(1, 6, 9, 12, 3, 2, 8, 11)
maior(2, 6, 2)
