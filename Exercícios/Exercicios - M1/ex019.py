print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\nFaça um programa que ajude ele, lendo o nome deles e escrevendo o do nome do escolhido.')
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}!')

from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}!')




