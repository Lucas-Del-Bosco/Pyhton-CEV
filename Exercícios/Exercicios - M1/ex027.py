print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente')

nome = str(input('Escreva seu nome completo: ')).strip().title()
n = nome.split()
print(f'O seu nome completo é {nome}.')
print(f'O seu primeiro nome é {n[0]}')
print(f'O seu último nome é {n[-1]}')
















