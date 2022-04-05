print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')

num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\33[33m{c}', end=' ')
        cont += 1
    else:
        print(f'\33[31m{c}', end=' ')
print(f'\n\033[mO número {num} é divisível por {cont} números!')
if cont == 2:
    print('Este número É PRIMO!')
else:
    print('Este número NÃO É PRIMO!')
