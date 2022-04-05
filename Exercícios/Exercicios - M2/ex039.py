print('Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.\nSeu programa também deverá mostrar o tempo que falta ou que passou do prazo.')

from datetime import date
ano = int(input('Qual é o ano de nascimento?: '))
idade = date.today().year - ano
if idade > 18:
    print(f'Você tem {idade} anos. Vá URGENTEMENTE à junta militar para regularizar suas obrigações!')
elif idade == 18:
    print(f'Você tem {idade} anos. Fique atento às datas corretas para o alistamento neste ano!')
elif idade < 18:
    print(f'Você tem {idade} anos. Ainda faltam {(18 - idade)} anos para o seu alistamento!')
