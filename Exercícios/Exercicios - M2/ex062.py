print('Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.')

n = int(input('Digite o primeiro valor da PA: '))
r = int(input('Digite a razão: '))
cont = 0
total = 10
mais = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{n} >', end=' ')
        cont += 1
        n += r
    print('PAUSE')
    mais = int(input('\nQuantos termos você quer adicionar?: '))
print(f'Progressão finalizada com {cont} termos. FIM')



