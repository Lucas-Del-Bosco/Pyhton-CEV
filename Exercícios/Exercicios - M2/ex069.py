#print('Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:\nA) quantas pessoas tem mais de 18 anos.\nB) quantos homens foram cadastrados.\nC) quantas mulheres tem menos de 20 anos.')

homens = mulheres = maiores = cont = 0
continuar = 'S'
while continuar == 'S':
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print(f'''Ao todo foram {cont} pessoas cadastradas, sendo:
{maiores} pessoas maiores de 18 anos;
{homens} homens cadastrados;
{mulheres} mulheres com menos de 20 anos.''')
