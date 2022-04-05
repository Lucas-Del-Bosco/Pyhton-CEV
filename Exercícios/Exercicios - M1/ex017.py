print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')

co = float(input('Qual o valor do cateto oposto?: '))
ca = float(input('Qual o valor do cateto adjacente?:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hiponetusa é de {hi:.2f}!')

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'O valor da hipotenusa é de {hi:.2f}!')

from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa é de {hi:.2f}!')

