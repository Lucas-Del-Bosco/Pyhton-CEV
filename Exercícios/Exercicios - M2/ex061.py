print('Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.')

n = int(input('Digite o primeiro número da PA: '))
r = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print(f'{n} > ', end='')
    cont += 1
    n += r
print('FIM')
