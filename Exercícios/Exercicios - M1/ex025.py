print('Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.')

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.title().split()
print('Silva' in nome1)

nome = str(input('Digite o seu nome completo: ')).strip().title().split()
print('Silva' in nome)
