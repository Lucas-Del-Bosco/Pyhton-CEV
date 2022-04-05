#print('Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')

from datetime import date
hoje = date.today().year
pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
idade = hoje - nascimento
pessoa['Idade'] = idade
pessoa['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['Carteira'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = (pessoa['Contratação'] + 35) - hoje + pessoa['Idade']
    for k, v in pessoa.items():
        print(f'- {k} tem valor {v}')
else:
    for k, v in pessoa.items():
        print(f'- {k} tem valor {v}')
