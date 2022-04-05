#print('Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.')
from time import sleep
c = ('\033[m',          # 0 — SEM COR
     '\033[0;30;41m',   # 1 — VERMELHO
     '\033[0;30;42m',   # 2 — Verde
     '\033[0;30;43m',   # 3 — Amarelo
     '\033[0;30;44m',   # 4 — Azul
     '\033[0;30;45m',   # 5 — Roxo
     '\033[7;30m')      # 6 — Branco


def ajuda(txt):
    print(f'Acessando o manual de comando \'{txt}\'', 4)
    sleep(1.5)
    print(c[3], end='')
    help(txt)
    print(c[0], end='')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
título('BEM-VINDO AO SISTEMA DE AJUDA PyHELP!', 2)
comando = ''
while True:
    comando = str(input('Função ou Biblioteca > : ')).lower().strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
