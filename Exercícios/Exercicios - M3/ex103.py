#print('Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.')

def ficha(nome='', gols=''):
    if nome == '':
        nome = 'desconhecido'
    if not gols.isdigit():
        gols = 0
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato!')


jogador = str(input('Nome do Jogador: ')).strip().title()
gols_marcados = str(input('Quantos gols marcados?: ')).strip()
ficha(jogador, gols_marcados)
