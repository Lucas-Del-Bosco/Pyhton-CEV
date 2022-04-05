#print('Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média')

lista = []
mulheres = []
maiormedia = []
pessoas = dict()
somidade = 0
while True:
    pessoas['Nome'] = str(input('Nome: ')).strip().title()
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip()[0].upper()
    while pessoas['Sexo'] not in 'MmFf':
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip()[0].upper()
    pessoas['Idade'] = int(input('Idade: '))
    somidade += pessoas['Idade']
    lista.append(pessoas.copy())
    pessoas.clear()
    continuar = str(input('Quer adicionar mais pessoas? [S/N]: ')).strip()[0].upper()
    while continuar not in 'SsNn':
        continuar = str(input('Quer adicionar mais pessoas? [S/N]: ')).strip()[0].upper()
    if continuar not in 'Ss':
        break
print('=-' * 25)
print(f'A) Foram cadastradas {len(lista)} pessoas!')
print(f'B) A média de idade foi de {somidade / len(lista)} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'D) As pessoas com idade acima da média são: ', end='')
for p in lista:
    if p['Idade'] > somidade / len(lista):
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<< ENCERRADO >>')
