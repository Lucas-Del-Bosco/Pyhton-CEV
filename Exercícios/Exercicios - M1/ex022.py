print('''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.''')

nome = str(input('Qual é o seu nome completo?: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
letras = len(nome) - nome.count(' ')
divisao = nome.split()
pnome = divisao[0]
letraspnome = len(pnome)
print(f'O seu nome completo em maiúsculo é {maiusculo}')
print(f'O seu nome completo em minúsculo é {minusculo}')
print(f'A quantidade de letras do seu nome é {letras} letras.')
print(f'Seu primeiro nome é {pnome} e ele tem {letraspnome} letras.')

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'O seu nome em maiúsculo é {nome.upper()}')
print(f'O seu nome minúsculo é {nome.lower()}')
letras = len(nome) - nome.count(' ')
print(f'A quantidade de letras do seu nome é de {letras}!')
separa = nome.split()
print(f'{separa}')
print(f'O seu primeiro nome é {separa[0]} e a quantidade de letras é {len(separa[0])}')








