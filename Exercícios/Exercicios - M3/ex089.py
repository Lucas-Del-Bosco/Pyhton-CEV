#print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')

lista = []
temporario = []
while True:
    nome = str(input('Nome do Aluno: ')).strip().title()
    temporario.append(nome)
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    temporario.append(n1)
    temporario.append(n2)
    média = (n1 + n2) / 2
    temporario.append(média)
    lista.append(temporario[:])
    temporario.clear()
    continuar = str(input('Quer adicionar mais alunos? [S/N]: '))
    if continuar not in 'Ss':
        break
print('=-' * 15)
print(f'{"NO.":<4} {"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10}{a[3]:>7.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno?: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]} e {lista[opc][2]}')
print('Volte sempre!')
