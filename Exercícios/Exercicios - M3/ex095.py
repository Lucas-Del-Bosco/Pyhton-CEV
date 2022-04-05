#print('Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.')

listajogadores = []
jogador = {}
lista = []
gols = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou?: '))
    for c in range(1, part + 1):
        gol = int(input(f'Quantos gols na {c}ª partida?: '))
        gols += gol
    lista.append(gol)
    jogador['Partidas'] = lista.copy()
    jogador['Gols'] = gols
    listajogadores = jogador.copy()
    continuar = str(input('Quer adicionar outro jogador? [S/N]: ')).strip()[0].upper()
    while continuar not in 'SsNn':
        continuar = str(input('Quer adicionar outro jogador? [S/N]: ')).strip()[0].upper()
    if continuar in 'Nn':
        break
print('=-' * 8, 'DESEMPENHO DO JOGADOR', '=-' * 8)

print(f'O jogador {listajogadores[jogador["Nome"]]} jogou {part} partidas, e fez {gols} gols, sendo:')


'''for i, g in listajogadores.keys():
    print(f' => Na partida {i}, o jogador fez {g} gols!')'''

'''time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantos jogos o jogador {jogador["nome"]} fez?: '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'Quandos gols na {c}ª partida?: ')))
    jogador['gols'] = partidas.copy()
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Quer adicionar mais jogadores? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer adicionar mais jogadores? [S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('=-' * 30)
for k, v in enumerate(time):
    print(f'{k+1:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas e marcou {jogador["total"]} gols, sendo: ')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na {i+1}ª partida, fez {v} gols!')'''



