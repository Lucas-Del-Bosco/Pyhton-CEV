#print('Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:\nA) Quantas pessoas foram cadastradas.\nB) Uma listagem com as pessoas mais pesadas.\nC) Uma listagem com as pessoas mais leves.')

grupo = []
pessoa = []
cadastro = maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if cadastro == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]
    cadastro += 1
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {cadastro} pessoas no sistema.')
print(f'A pessoa mais pesada é: ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}, pesando {p[1]}kg!')
print()
print(f'A pessoa mais leve é: ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}, pesando {p[1]}kg!')
