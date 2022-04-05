print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O seno desse ângulo é {seno:.2f}.\nO cosseno desse ângulo é {cos:.2f}.\nA tangente desse ângulo é {tan:.2f}.')

from math import sin, cos, tan, radians
angulo = float(input('Qual o ângulo?: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O valor do seno é {sen:.2f}.\nO valor do cosseno é {cos:.2f}.\nO valor da tangente é {tan:.2f}.')