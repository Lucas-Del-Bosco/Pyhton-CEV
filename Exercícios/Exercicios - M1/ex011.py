print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária\npara pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²: ')

a = float(input('Qual é a altura da sua parede?: '))
l = float(input('Qual é a largura da sua parede?: '))

print(f'A medida da sua parede é de {a}m x {l}m, totalizando assim {a*l:.2f}m²\nPortanto, como cada litro de tinta consegue pintar 2m², a quantidade necessária de tinta para pintar a sua parede por completo é de {a*l/2:.2f} litros.')
