print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto: ')

vp = float(input('Valor do produto: R$ '))
vpd = vp * 0.95

print(f'O produto custa R${vp:.2f}, com o desconto de 5% aplicado, o produto passa a custar R${vpd:.2f}.')

