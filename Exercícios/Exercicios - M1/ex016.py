print('Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.')
import math
num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {math.floor(num)}!')

from math import trunc, floor
print(f'O valor digitado foi {num} e a sua porção inteira é {floor(num)}!')

print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}!')

print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}!')




