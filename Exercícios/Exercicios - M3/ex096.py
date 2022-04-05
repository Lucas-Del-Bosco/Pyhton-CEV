#print('Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.')
def lin():
    print('-' * 20)


def area(larg, comp):
    print('-' * 42)
    print(f'A área de um terreno {larg} x {comp} é de {larg*comp}m²')
    print('-' * 42)


lin()
print('CONTROLE DE TERRENO')
lin()
l = float(input('Largura [m]: '))
c = float(input('Comprimento [m]: '))
area(l, c)

