#print('Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
resp = 'S'
while resp == 'S':
    escolha = int(input('Digite um número de 0 a 10: '))
    if 0 <= escolha <= 10:
        print(f'O número que vocês escolheu escrito por extenso é {números[escolha]}!')
        resp = str(input('Você quer continuar?: ')).upper().strip()[0]
    else:
        print('O número que você digitou não é válido!')
print('Programa finalizado!')
