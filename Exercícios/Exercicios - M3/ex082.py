#print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.')

valores = []
pares = []
ímpares = []
while True:
    n = (int(input('Digite um valor: ')))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
    resposta = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if resposta in 'Nn':
        break
valores.sort()
pares.sort()
ímpares.sort()
print(f'Os números digitados foram {valores}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {ímpares}')
