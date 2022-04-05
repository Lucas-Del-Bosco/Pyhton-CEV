#print('Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:\na) de 1 até 10, de 1 em 1\nb) de 10 até 0, de 2 em 2\nc) uma contagem personalizada')

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 30)
    print(f'CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}')
    print('~' * 30)
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont += p
        print('FIM')
        print('~' * 30)
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont -= p
        print('FIM')
        print('~' * 30)
        print()


#ENUNCIADO a) e b)
contador(1, 10, 1)
contador(10, 0, 2)

#ENUNCIADO c)
print('AGORA É A SUA VEZ DE PERSONALIZAR')
print()
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
