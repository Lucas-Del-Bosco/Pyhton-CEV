print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.')

sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'M F':
    sexo = str(input('Dados Inválidos. Digite o seu sexo: ')).strip()[0].upper()
print(f'Sexo {sexo} registrado com sucesso.')
