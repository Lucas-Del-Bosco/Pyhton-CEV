print('Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.')

somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
mulheres = 0
for p in range(1, 5):
    print(f'{p}ª pessoa:')
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    elif idade > maiorhomem and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        mulheres += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos!')
print(f'O homem mais velho tem {maiorhomem} anos e seu nome é {nomevelho}!')
print(f'A quantidade de mulheres com menos de 20 anos é de {mulheres}!')
