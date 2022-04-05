print('Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\n– O primeiro valor é maior\n– O segundo valor é maior\n– Não existe valor maior, os dois são iguais')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor é MAIOR do que o segundo.')
elif n1 < n2:
    print('O segundo valor é MAIOR do que o primeiro.')
elif n1 == n2:
    print('Os dois valores são IGUAIS.')
