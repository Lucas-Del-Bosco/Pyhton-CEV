#print('Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.')

aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 6.0:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'{aluno["nome"]} ficou com a média {aluno["média"]}, e por isso está {aluno["situação"]}!')
