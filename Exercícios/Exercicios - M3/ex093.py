#print('Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.')

desempenho = {}
partidas = []
desempenho['Nome'] = str(input('Nome do Jogador: ')).strip().title()
totpartidas = int(input(f'Número de partidas que {desempenho["Nome"]} jogou: '))
for g in range(1, totpartidas + 1):
    partidas.append(int(input(f'Quantos gols na {g}ª partida?: ')))
desempenho['Gols'] = partidas.copy()
desempenho['Total'] = sum(partidas)
print('=-' * 25)
print(f'{desempenho}')
print('=-' * 25)
for v, k in desempenho.items():
    print(f'O campo {v} tem valor {k}!')
print('=-' * 25)
print(f'O jogador {desempenho["Nome"]} jogou {totpartidas} partidas.')
for p, g in enumerate(partidas):
    print(f'Na partida {p + 1}, {desempenho["Nome"]} fez {g} gols!')
print(f'Totalizando {sum(partidas)} gols na temporada!')







