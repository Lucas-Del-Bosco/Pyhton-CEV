import moeda
from os import system

valor = float(input('Qual o preço do produto? R$'))
print('''Escolha uma opção:
[1] - Aumentar o preço em %
[2] - Diminuir o preço em %
[3] - Dobrar o preço
[4] - Reduzir o preço na metade''')
opção = int(input('Sua opção: '))
while True:
    if opção == 1:
        taxa = float(input('Qual a taxa a ser considerada?: '))
        total = moeda.aumentar(valor, taxa)
        print(f'O valor após a aplicação da taxa de {taxa}% é de R${total}!')
    elif opção == 2:
        taxa = float(input('Qual a taxa a ser considerada?: '))
        total = moeda.diminuir(valor, taxa)
        print(f'O valor após a aplicação da taxa de {taxa}% é de R${total}!')
    elif opção == 3:
        valor *= 2
        print(f'O valor após a duplicação do valor é de R${valor}!')
    elif opção == 4:
        valor /= 2
        print(f'O valor após reduzir pela metade é de R${valor}!')
    elif opção != '1234':
        print(f'Opção desconhecida, por favor selecionar uma opção válida.')
        opção = int(input('Sua opção: '))
