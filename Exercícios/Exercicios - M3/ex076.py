#print('Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.')

listagem = ('Caderno', 5.90,
            'Lápis', 1.99,
            'Mochila', 99.90,
            'Estojo', 24.99,
            'Corretivo', 7.49,
            'Tesoura', 3.99,
            'Caneta', 2.99,
            'Cartolina', 0.49)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
